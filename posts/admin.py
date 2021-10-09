from django.contrib import admin
from .models import AnswerPost, WalkthroughPost, QuestionPost, FAQPost
# Register your models here.
admin.site.register(QuestionPost)
admin.site.register(FAQPost)
admin.site.register(AnswerPost)
admin.site.register(WalkthroughPost)