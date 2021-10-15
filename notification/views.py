from django.shortcuts import render, reverse

from notification.models import Notification
from django.views.generic import View

# Create your views here.
class NotificationView(View):
    def get(self, request):
        notifications = Notification.objects.filter(mentioned=request.user).order_by('-id')
        for notification in notifications:
            notification.delete()
        return render(request, 'notification.html', {'notifications': notifications})