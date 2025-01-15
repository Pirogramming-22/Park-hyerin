from django.db import models
from django.urls import reverse

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ideas/')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey('devTools.DevTool', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ideas:detail', args=[self.id])

class IdeaStar(models.Model):
    idea = models.OneToOneField(Idea, on_delete=models.CASCADE)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.idea.title} - Starred: {self.is_starred}"