from django import forms
from posts.models import CommentPost, QuestionPost, FAQPost
from users.models import MyUser

class AddCommentPost(forms.ModelForm):
    post_img = forms.ImageField(required=True)
    class Meta:
        model = CommentPost
        fields = ('post_title', 'post_body','creator', 'date_created')

class AddQuestionPost(forms.Form):
    question_title = forms.CharField(max_length=200)
    question_body = forms.CharField(max_length=200)
    question_img = forms.ImageField(required=True)

    question = forms.ChoiceField(choices=[(True, 'Question'),(False, 'Answer')])

class AddFAQPost(forms.Form):
    faq_title = forms.CharField(max_length=250)
    faq_body = forms.CharField(max_length=250)
    faq_img = forms.ImageField(required=True)
