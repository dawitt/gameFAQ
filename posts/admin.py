from django.contrib import admin
from .models import AnswerPost, CommentPost, QuestionPost, FAQPost
# Register your models here.
admin.site.register(CommentPost)
admin.site.register(QuestionPost)
admin.site.register(FAQPost)
admin.site.register(AnswerPost)