from django.db import models
from users.models import MyUser
from django.utils import timezone
from PIL import Image
# Create your models here.

class QuestionPost(models.Model):
    question_title = models.CharField(max_length=200)
    question_body = models.CharField(max_length=250)
    question_img = models.ImageField(upload_to='uploaded_imgages/', null=True, blank=True)
    question_creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    for_game = models.CharField(max_length=100)
    
    def __str__(self):
        return self.question_title

class AnswerPost(models.Model):
    answer_body = models.TextField()
    answer_img = models.ImageField(upload_to='uploaded_imgages/', null=True, blank=True)
    question = models.ForeignKey(QuestionPost, on_delete=models.CASCADE)
    answer_creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_body


class WalkthroughPost(models.Model):
    walkthrough_title = models.CharField(max_length=100)
    walkthrough_body = models.TextField()
    walkthrough_img = models.ImageField(upload_to='uploaded_imgages/', null=True, blank=True)
    walkthrough_creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    for_game = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.walkthrough_title

class WalkthroughComment(models.Model):
    post_body = models.TextField()
    walkthrough_post = models.ForeignKey(WalkthroughPost, on_delete=models.CASCADE)
    post_img = models.ImageField(upload_to='uploaded_imgages/', null=True, blank=True)
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    for_game = models.CharField(max_length=100)

    def __str__(self):
        return self.post_body
