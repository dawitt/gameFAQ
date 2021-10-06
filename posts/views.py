from django import forms
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import AddCommentPost, AddQuestionPost, AddFAQPost
from users.models import MyUser
from posts.models import CommentPost, QuestionPost, FAQPost
from notification.models import Notification
from django.views.generic import View 
# Create your views here.

def homepage_view(request):
    user = request.user
    form = AddQuestionPost()
    return render(request, 'index.html', {'user':user})


class Question_detail_view(View):
    def get(self, request, id):
        question_post = QuestionPost.objects.get(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':question_post})



class Comment_detail_view(View):
    def get(self, request, id):
        comment_post = CommentPost.objects.get(id=id)
        return render(request, 'generic_post_detail.html', {'comment_post':comment_post})

class Faq_detail_view(View):
    def get(self, request, id):
        faq_post = FAQPost.objects.get(id=id)
        return render(request, 'generic_post_detail.html', {'faq_post':faq_post})


def add_comment(request):
    if request.method == 'POST':
        form = AddCommentPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            comment = CommentPost.objects.create(
                post_title = data['post_title'],
                post_body = data['post_body'],
                post_img = data['post_img'],
                creator = request.user
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('home'))
    form = AddCommentPost()
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
                question = data['question']
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('home'))
    form = AddQuestionPost()
    return render(request, 'generic_form.html', {'form':form})

def add_faq(request):
    if request.method == 'POST':
        form = AddFAQPost(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            comment = FAQPost.objects.create(
                faq_title = data['faq_title'],
                faq_body = data['faq_body'],
                faq_img = data['faq_img'],
                faq_creator = request.user
            )
            # breakpoint()
            return HttpResponseRedirect(reverse('home'))
    form = AddFAQPost()
    return render(request, 'generic_form.html', {'form':form})
