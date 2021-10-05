from django.shortcuts import render
from users.models import MyUser
from posts.models import QuestionPosts, CommentPosts, FAQPosts
from django.views.generic import View
# Create your views here.

class User_detail_view(View):
    def get(self, request, id):
        user = MyUser.objects.get(id=id)
        questions = QuestionPosts.objects.filter(question_creator=user)
        comments = CommentPosts.objects.filter(creator=user)
        faqs = FAQPosts.objects.filter(faq_creator=user)
        return render(request, 'user_detail.html', {'user': user, 'questions':questions, 'comments': comments, 'faqs':faqs})
        

