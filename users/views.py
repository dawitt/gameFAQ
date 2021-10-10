from django.shortcuts import render
from users.models import MyUser
from posts.models import QuestionPost, WalkthroughPost, WalkthroughComment
from django.views.generic import View
# Create your views here.

class UserDetailView(View):
    def get(self, request, id):
        user = MyUser.objects.get(id=id)
        questions = QuestionPost.objects.filter(question_creator=user)
        walkthroughs = WalkthroughPost.objects.filter(walkthrough_creator=user)
        return render(request, 'user_detail.html', {'user': user, 'questions':questions, 'walkthroughs': walkthroughs})

def all_users(request):
    users = MyUser.objects.all()
    return render(request, 'all_users.html', {'users': users})

