from django import forms
from CBVPractice.Profile.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

