from django.db import models
from users.models import MyUser
from posts.models import AnswerPost, WalkthroughPost, QuestionPost, WalkthroughComment
# Create your models here.
class Notification(models.Model):
    
    mentioned = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='mentioned')
    walkthrough_post = models.ForeignKey(WalkthroughPost, on_delete=models.CASCADE, related_name='walkthrough_post', blank=True, null=True)
    question_post = models.ForeignKey(QuestionPost, on_delete=models.CASCADE, related_name='question_post', blank=True, null=True)
    comment_post = models.ForeignKey(WalkthroughComment, on_delete=models.CASCADE, related_name='comment_post', blank=True, null=True)
    answer_post = models.ForeignKey(AnswerPost, on_delete=models.CASCADE, related_name='answer_post', blank=True, null=True )
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.mentioned.username