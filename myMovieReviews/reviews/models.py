from django.db import models

# Create your models here.
class MovieReview(models.Model):
    GENRE_CHOICES = [
        ('action', '액션'),
        ('comedy', '코미디'),
        ('drama', '드라마'),
        ('horror', '공포'),
        ('fantasy', '판타지'),
        ('SF', '공상과학'),
        ('musical', '뮤지컬'),
        ('history', '역사'),
        ('mystery', '미스터리'),
        ('documentary', '다큐'),
        ('animation', '애니메이션')
    ]
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, verbose_name="장르" )
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    runtime = models.PositiveIntegerField()  # minutes
    review_content = models.TextField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title