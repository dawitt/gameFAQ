from django.shortcuts import render, HttpResponseRedirect, reverse
from users.models import MyUser
from posts.models import WalkthroughPost, WalkthroughComment, QuestionPost, AnswerPost
from notification.models import Notification
from django.views.generic import View

# Create your views here.
class NotificationView(View):
    def get(self, request):
        notifications = Notification.objects.all().order_by('-id')
        for notification in notifications:
            notification.delete()
        return render(request, 'notification.html', {'notifications': notifications})