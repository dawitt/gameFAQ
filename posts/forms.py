from django import forms
from posts.models import CommentPost, QuestionPost, FAQPost
from users.models import MyUser

class AddCommentPost(forms.ModelForm):
    post_img = forms.ImageField(required=False)
    class Meta:
        model = CommentPost
        fields = ('post_title', 'post_body','creator', 'date_created', 'for_game')

class AddQuestionPost(forms.Form):
    question_title = forms.CharField(max_length=200)
    question_body = forms.CharField(max_length=200)
    question_img = forms.ImageField(required=False)
    for_game = forms.CharField(max_length=100)
    

class AddFAQPost(forms.Form):
    faq_title = forms.CharField(max_length=250)
    faq_body = forms.CharField(max_length=250)
    faq_img = forms.ImageField(required=False)
    for_game = forms.CharField(max_length=100)

class AddAnswerForm(forms.Form):
    answer_body = forms.CharField(max_length=250)
    answer_img = forms.ImageField(required=False)
    
