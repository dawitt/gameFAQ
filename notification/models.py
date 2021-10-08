from django.db import models
from users.models import MyUser
from posts.models import CommentPost, QuestionPost, FAQPost
# Create your models here.
class Notification(models.Model):
    
    mentioned = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mentioned')
    comment_post = models.ForeignKey(CommentPost, on_delete=models.CASCADE, related_name='comment_post', blank=True, null=True)
    question_post = models.ForeignKey(QuestionPost, on_delete=models.CASCADE, related_name='question_post', blank=True, null=True)
    faq_post = models.ForeignKey(FAQPost, on_delete=models.CASCADE, related_name='faq_post', blank=True, null=True)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.post