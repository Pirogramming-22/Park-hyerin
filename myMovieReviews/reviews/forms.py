from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'actors', 'genre', 'rating', 'runtime', 'review_content', 'release_year']
        labels = {
            'title': '영화 제목',  
            'director': '감독',  
            'actors': '주연',  
            'genre': '장르',  
            'rating': '별점',  
            'runtime': '러닝타임',  
            'review_content': '리뷰 내용',  
            'release_year': '개봉년도',  
        }

        genre = forms.ChoiceField(
            choices=MovieReview.GENRE_CHOICES,  
            widget=forms.Select,  
        )
