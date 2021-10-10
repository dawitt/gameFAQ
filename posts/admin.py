from django.contrib import admin
from .models import AnswerPost, WalkthroughPost, QuestionPost, WalkthroughComment
# Register your models here.
admin.site.register(QuestionPost)
admin.site.register(WalkthroughPost)
admin.site.register(AnswerPost)
admin.site.register(WalkthroughComment)