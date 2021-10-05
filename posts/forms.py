from django import forms
from posts.models import CommentPosts, QuestionPosts, FAQPosts
from users.models import MyUser

class AddCommentPost(forms.ModelForm):
    class Meta:
        model = CommentPosts
        fields = ('post_title', 'post_body', 'creator', 'date_created')

class AddQuestionPost(forms.Form):
    question_title = forms.CharField(max_length=200)
    question_body = forms.CharField(max_length=200)
    question = forms.ChoiceField(choices=[(True, 'Question'),(False, 'Answer')])

class AddFAQPost(forms.Form):
    faq = forms.CharField(max_length=250)
    