from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'actors', 'genre', 'rating', 'runtime', 'review_content', 'release_year']