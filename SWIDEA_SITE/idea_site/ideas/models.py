from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Idea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ideas/')
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.ForeignKey('devTools.DevTool', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ideas:detail', args=[self.id])

class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    starred_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'idea')
