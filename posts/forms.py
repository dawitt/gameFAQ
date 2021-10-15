from django import forms
from posts.models import WalkthroughComment

class AddWalkthroughComment(forms.ModelForm):
    post_img = forms.ImageField(required=False)
    class Meta:
        model = WalkthroughComment
        fields = ('post_body',)

class AddQuestionPost(forms.Form):
    question_title = forms.CharField(max_length=200)
    question_body = forms.CharField(widget=forms.Textarea)
    question_img = forms.ImageField(required=False)

class AddWalkthroughPost(forms.Form):
    walkthrough_title = forms.CharField(max_length=250)
    walkthrough_body = forms.CharField(widget=forms.Textarea)
    walkthrough_img = forms.ImageField(required=False)

class AddAnswerForm(forms.Form):
    answer_body = forms.CharField(widget=forms.Textarea)
    answer_img = forms.ImageField(required=False)
