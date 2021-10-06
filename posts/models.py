from django.db import models
from users.models import MyUser
from django.utils import timezone
from PIL import Image
# Create your models here.
class CommentPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_body = models.CharField(max_length=250)
    post_img = models.ImageField(upload_to='uploaded_images/')
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title

class QuestionPost(models.Model):
    question_title = models.CharField(max_length=200)
    question_body = models.CharField(max_length=250)
    question_creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    question = models.BooleanField()

    def __str__(self):
        return self.question_title


class FAQPost(models.Model):
    faq = models.TextField(max_length=250)
    faq_creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.faq