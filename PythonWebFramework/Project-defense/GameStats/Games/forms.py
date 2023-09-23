from django import forms
from GameStats.Games.models import Game, Comment


class GameForm(forms.ModelForm):
    creator = forms.CharField(disabled=True)

    class Meta:
        model = Game
        fields = '__all__'


class CommentGameForm(forms.ModelForm):
    game = forms.CharField(disabled=True)
    creator = forms.CharField(disabled=True)
    comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Comment"}), label='')

    class Meta:
        model = Comment
        fields = '__all__'
