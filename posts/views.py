from django import forms
from django.shortcuts import render, HttpResponseRedirect, reverse
import notification
from posts.forms import AddWalkthroughComment, AddQuestionPost, AddWalkthroughPost, AddAnswerForm
from users.models import MyUser
from posts.models import WalkthroughComment, QuestionPost, WalkthroughPost, AnswerPost
from notification.models import Notification
from django.views.generic import View 
import requests
import json
from django.template import RequestContext
# Create your views here.

class HomepageView(View):
    def get(self, request):
        user = request.user
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
            notification = Notification.objects.create(
                mentioned = question_post.question_creator,
                question_post = question_post,
                answer_post = new_answer,
                
            )
        #return HttpResponseRedirect(reverse('question_detail'))
    answers = AnswerPost.objects.filter(question=question_post)
    form = AddAnswerForm()
    return render(request, 'question_detail.html', {'question_post':question_post, 'form':form, 'answers':answers})


def walkthrough_detail_view(request, id):
    walkthrough_post = WalkthroughPost.objects.get(id=id)
    if request.method == 'POST':
        form = AddWalkthroughComment(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            walkthrough_comment = WalkthroughComment.objects.create(
                post_body = data['post_body'],
                post_img = data['post_img'],
                walkthrough_post = walkthrough_post,
                creator = request.user, 
            )
            notification = Notification.objects.create(
                mentioned = walkthrough_post.walkthrough_creator,
                walkthrough_post = walkthrough_post,
                comment_post = walkthrough_comment,
                
            )
    form = AddWalkthroughComment()
    walkthrough_comments = WalkthroughComment.objects.filter(walkthrough_post=walkthrough_post)
    return render(request, 'game_walkthrough.html', {'form': form, 'walkthrough_post':walkthrough_post, 'walkthrough_comments': walkthrough_comments})

            #return HttpResponseRedirect(reverse('faq-detail', args=(id,)))

def like_answer(request, id):
    post = AnswerPost.objects.get(id=id)
    question = post.question.id
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('question-detail', args=(question,)))

def dislike_answer(request, id):
    post = AnswerPost.objects.get(id=id)
    question = post.question.id
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(reverse('question-detail', args=(question,)))

def like_walkthrough(request, id):
    post = WalkthroughPost.objects.get(id=id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('walkthrough', args=(id,)))

def dislike_walkthrough(request, id):
    post = WalkthroughPost.objects.get(id=id)
    post.dislikes += 1
    post.save()
    return HttpResponseRedirect(reverse('walkthrough', args=(id,)))

# def add_walkthrough(request, id):
#     walkthrough = WalkthroughPost.objects.get(id=id)
#     if request.method == 'POST':
#         form = AddWalkthroughComment(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             walkthrough_comment = WalkthroughComment.objects.create(
                
#                 post_body = data['post_body'],
#                 post_img = data['post_img'],
#                 walkthrough_post = walkthrough,
#                 creator = request.user,
#                 for_game = data['for_game']
#             )
#             # breakpoint()
#             return HttpResponseRedirect(reverse('walkthrough', args=(id,)))
#     form = AddWalkthroughComment()
#     return render(request, 'generic_form.html', {'form':form})

# def add_question(request):
#     if request.method == 'POST':
#         form = AddQuestionPost(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data
#             question = QuestionPost.objects.create(
#                 question_title = data['question_title'],
#                 question_body = data['question_body'],
#                 question_img = data['question_img'],
#                 question_creator = request.user,
#                 for_game = data['for_game']
#             )
#             # breakpoint()
#             return HttpResponseRedirect(reverse('home'))
#     form = AddQuestionPost()
#     return render(request, 'generic_form.html', {'form':form})

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

def add_walkthrough(request, id):
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
        form = AddWalkthroughPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            new_walkthrough = WalkthroughPost.objects.create(
                walkthrough_title = data['walkthrough_title'],
                walkthrough_body = data['walkthrough_body'],
                walkthrough_img = data['walkthrough_img'],
                walkthrough_creator = request.user,
                for_game = game_name
            )

            return HttpResponseRedirect(reverse('game_detail', args=(id,)))
    form = AddWalkthroughPost()
    return render(request, 'generic_form.html', {'form':form})


#Got404/500 info from: 
# https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page

# def handler404(request, *args, **argv):
#     response = render('404.html', {}, context_instance=RequestContext(request))
#     response.status_code = 404
#     return response


# INCASE: handler404 will fail with message:"handler404() got an unexpected keyword argument 'exception'"
# Use the next handler404 def instead.

# def handler404(request, exception, template_name="404.html"):
#     response = render_to_response(template_name)
#     response.status_code = 404
#     return response

# def handler500(request, *args, **argv):
#     response = render('500.html', {}, context_instance=RequestContext(request))
#     response.status_code = 500
#     return response

def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "400.html", {})