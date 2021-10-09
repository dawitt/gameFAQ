from django.shortcuts import render
from users.models import MyUser
from posts.models import QuestionPost, WalkthroughPost, FAQPost
from django.views.generic import View
# Create your views here.

class User_detail_view(View):
    def get(self, request, id):
        user = MyUser.objects.get(id=id)
        questions = QuestionPost.objects.filter(question_creator=user)
        walkthrough_comments = WalkthroughPost.objects.filter(creator=user)
        faqs = FAQPost.objects.filter(faq_creator=user)
        return render(request, 'user_detail.html', {'user': user, 'questions':questions, 'walkthrough_comments': walkthrough_comments, 'faqs':faqs})
        

