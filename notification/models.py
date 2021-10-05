from django.db import models
from django.db.models.fields import NullBooleanField
from users.models import MyUser
from posts.models import CommentPosts, QuestionPosts, FAQPosts
# Create your models here.
class Notifications(models.Model):
    
    mentioned = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mentioned')
    comment_post = models.ForeignKey(CommentPosts, on_delete=models.CASCADE, related_name='comment_post', blank=True, null=True)
    question_post = models.ForeignKey(QuestionPosts, on_delete=models.CASCADE, related_name='question_post', blank=True, null=True)
    faq_post = models.ForeignKey(FAQPosts, on_delete=models.CASCADE, related_name='faq_post', blank=True, null=True)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.post