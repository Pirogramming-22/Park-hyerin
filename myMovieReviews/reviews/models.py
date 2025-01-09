from django.db import models

# Create your models here.
class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    runtime = models.PositiveIntegerField()  # minutes
    review_content = models.TextField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title