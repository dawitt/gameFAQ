from django import forms
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import AddWalkthroughPost, AddQuestionPost, AddFAQPost, AddAnswerForm
from users.models import MyUser
from posts.models import WalkthroughPost, QuestionPost, FAQPost, AnswerPost
from notification.models import Notification
from django.views.generic import View 
import requests
import json
# Create your views here.

def homepage_view(request):
    user = request.user
    form = AddQuestionPost()
    return render(request, 'index.html', {'user':user})



def question_detail_view(request, id):
    question_post = QuestionPost.objects.get(id=id)
    if request.method == 'POST':
        form = AddAnswerForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_answer = AnswerPost.objects.create(
            answer_body = data['answer_body'],
            answer_img = data['answer_img'],
            answer_creator = request.user,
            question = question_post
        )
        #return HttpResponseRedirect(reverse('question_detail'))
    answers = AnswerPost.objects.filter(question=question_post)
    form = AddAnswerForm()
    return render(request, 'question_detail.html', {'question_post':question_post, 'form':form, 'answers':answers})



# class Walkthrough_detail_view(View):
#     def get(self, request, id):
#         comment_post = WalkthroughPost.objects.get(id=id)
#         return render(request, 'generic_post_detail.html', {'comment_post':comment_post})

class Faq_detail_view(View):
    def get(self, request, id):
        form = AddWalkthroughPost()
        faq_post = FAQPost.objects.get(id=id)
        walkthrough_comments = WalkthroughPost.objects.filter(faq_post=faq_post)
        return render(request, 'game_walkthrought.html', {'form': form, 'faq_post':faq_post, 'walkthrough_comments': walkthrough_comments})
    def post(self, request, id):
        faq = FAQPost.objects.get(id=id)
        form = AddWalkthroughPost(request.POST)  # request.File
        if form.is_valid():
            data = form.cleaned_data
            walkthrough_comment = WalkthroughPost.objects.create(
                
                post_body = data['post_body'],
                post_img = data['post_img'],
                faq_post = faq,
                creator = request.user,
                
            )
            form = AddWalkthroughPost()
            faq_post = FAQPost.objects.get(id=id)
            walkthrough_comments = WalkthroughPost.objects.filter(faq_post=faq_post)
            return render(request, 'game_walkthrought.html', {'form': form, 'faq_post':faq_post, 'walkthrough_comments': walkthrough_comments})

            #return HttpResponseRedirect(reverse('faq-detail', args=(id,)))

def add_walkthrough_comment(request, id):
    faq = FAQPost.objects.get(id=id)
    if request.method == 'POST':
        form = AddWalkthroughPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            walkthrough_comment = WalkthroughPost.objects.create(
                
                post_body = data['post_body'],
                post_img = data['post_img'],
                faq_post = faq,
                creator = request.user,
                for_game = data['for_game']
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('faq-detail', args=(id,)))
    form = AddWalkthroughPost()
    return render(request, 'generic_form.html', {'form':form})

def add_question(request):
    if request.method == 'POST':
        form = AddQuestionPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            question = QuestionPost.objects.create(
                question_title = data['question_title'],
                question_body = data['question_body'],
                question_img = data['question_img'],
                question_creator = request.user,
                for_game = data['for_game']
                
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('home'))
    form = AddQuestionPost()
    return render(request, 'generic_form.html', {'form':form})

def ask_game_question(request, id):

    url = 'https://api.rawg.io/api/games/' + str(id)
    headers={
        'User-Agent': 'Q4_Capstone',
    }
    payload={
            'key':'81ea352e06b54bb4b1218cb8d2b0e4eb',
               
    }
    response = requests.get(url, headers=headers, params=payload)
    res_data = json.loads(response.text)
    game_name = res_data['name']
        # game_slug = data['slug']
    game_img = res_data['background_image']
    res_data = json.dumps(res_data, indent=2)

    if request.method == 'POST':
        form = AddQuestionPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            question = QuestionPost.objects.create(
                question_title = data['question_title'],
                question_body = data['question_body'],
                question_img = data['question_img'],
                question_creator = request.user,
                for_game = game_name
                
            )
            questions = QuestionPost.objects.filter(for_game=game_name)
            return HttpResponseRedirect(reverse('game_detail', args=(id,)))
            # render(request, 'game_walkthrought.html', {'game_name':game_name, 'game_img':game_img, 'questions':questions})
    form = AddQuestionPost()
    return render(request, 'generic_form.html', {'form':form})

def add_faq(request, id):
    url = 'https://api.rawg.io/api/games/' + str(id)
    headers={
        'User-Agent': 'Q4_Capstone',
    }
    payload={
            'key':'81ea352e06b54bb4b1218cb8d2b0e4eb',
                  
    }
    response = requests.get(url, headers=headers, params=payload)
    res_data = json.loads(response.text)
    game_name = res_data['name']
        # game_slug = data['slug']
    game_img = res_data['background_image']
    res_data = json.dumps(res_data, indent=2)


    if request.method == 'POST':
        form = AddFAQPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_faq = FAQPost.objects.create(
                faq_title = data['faq_title'],
                faq_body = data['faq_body'],
                faq_img = data['faq_img'],
                faq_creator = request.user,
                for_game = game_name
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('game_detail', args=(id,)))
    form = AddFAQPost()
    return render(request, 'generic_form.html', {'form':form})


# def add_answer(request, id):
#     if request.method == 'POST':
#         form = AddAnswerForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             answer = AnswerPost.objects.create(
#                 answer_body = data['answer_body'],
#                 answer_img = data['answer_img'],
#                 answer_creator = request.user,
#                 for_game = data['for_game']
#             )
#             # breakpoint()
#             return HttpResponseRedirect(reverse('home'))
#     form = AddAnswerForm()
#     return render(request, 'generic_form.html', {'form':form})

def all_questions(request):
    questions = QuestionPost.objects.all()
    if request.method == 'POST':
        form = AddQuestionPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            question = QuestionPost.objects.create(
                question_title = data['question_title'],
                question_body = data['question_body'],
                question_img = data['question_img'],
                question_creator = request.user,
                for_game = data['for_game']
                
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('all_questions'))
    form = AddQuestionPost()
    return render(request, 'all_questions.html', {'questions': questions, 'form': form})