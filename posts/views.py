from django import forms
from django.shortcuts import render, HttpResponseRedirect, reverse
from posts.forms import AddQuestionPost
from users.models import MyUser
from posts.models import CommentPosts, QuestionPosts, FAQPosts
from notification.models import Notifications
from django.views.generic import View 
# Create your views here.

def homepage_view(request):
    user = request.user
    form = AddQuestionPost()
    return render(request, 'index.html', {'user':user})


class Question_detail_view(View):
    def get(self, request, id):
        question_post = QuestionPosts.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':question_post})



class Comment_detail_view(View):
    def get(self, request, id):
        comment_post = CommentPosts.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':comment_post})

class Faq_detail_view(View):
    def get(self, request, id):
        faq_post = FAQPosts.objects.filter(id=id)
        return render(request, 'generic_post_detail.html', {'question_post':faq_post})
