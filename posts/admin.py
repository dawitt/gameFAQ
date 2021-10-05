from django.contrib import admin
from .models import CommentPosts, QuestionPosts, FAQPosts
# Register your models here.
admin.site.register(CommentPosts)
admin.site.register(QuestionPosts)
admin.site.register(FAQPosts)