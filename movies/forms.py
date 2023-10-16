from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    selects = [('Comedy','Comedy'), ('Fantasy', 'Fantasy'), ('Romance', 'Romance')]
    genre = forms.ChoiceField(choices=selects, widget=forms.Select, label='장르')
    score = forms.FloatField(
        label='평점',
        min_value=0,
        max_value=5,
        widget=forms.NumberInput(attrs={'step': 0.5})
    )
    
    class Meta:
        model = Movie
        fields = ('title', 'content', 'image', 'genre', 'score',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글')
    
    class Meta:
        model = Comment
        fields = ('content',)