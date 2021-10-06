from django import forms
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import AddCommentPost, AddQuestionPost
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
        question_post = QuestionPost.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':question_post})



class Comment_detail_view(View):
    def get(self, request, id):
        comment_post = CommentPost.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':comment_post})

class Faq_detail_view(View):
    def get(self, request, id):
        faq_post = FAQPost.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':faq_post})


def add_comment(request):
    if request.method == 'POST':
        form = AddCommentPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = CommentPost.objects.create(
                post_title = data['post_title'],
                post_body = data['post_body'],
                post_img = data['post_img'],
                creator = request.user
            )
            return HttpResponseRedirect(reverse('home'))
    form = AddCommentPost()
    return render(request, 'generic_form.html', {'form':form})
