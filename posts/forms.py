from django import forms
from posts.models import WalkthroughPost, QuestionPost, FAQPost
from users.models import MyUser

class AddWalkthroughPost(forms.ModelForm):
    post_img = forms.ImageField(required=False)
    class Meta:
        model = WalkthroughPost
        fields = ('post_body',)

class AddQuestionPost(forms.Form):
    question_title = forms.CharField(max_length=200)
    question_body = forms.CharField(max_length=200)
    question_img = forms.ImageField(required=False)
    
    

class AddFAQPost(forms.Form):
    faq_title = forms.CharField(max_length=250)
    faq_body = forms.CharField(max_length=250)
    faq_img = forms.ImageField(required=False)

class AddAnswerForm(forms.Form):
    answer_body = forms.CharField(max_length=250)
    answer_img = forms.ImageField(required=False)
    
