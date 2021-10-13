from django import forms
# from api.forms import Game

class AddGameInfo(forms.ModelForm):
    game_name = forms.CharField(max_length=100)
    game_slug = forms.CharField(max_length=100)
    game_release = forms.DateTimeField()
    game_img = forms.ImageField(required=False)
    game_desc = forms.CharField(max_length=400)
    esrb_rating = forms.CharField(max_length=10)
    platform = forms.CharField(max_length=100)
