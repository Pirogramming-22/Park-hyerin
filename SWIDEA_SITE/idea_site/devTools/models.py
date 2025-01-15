from django.db import models
from django.urls import reverse

class DevTool(models.Model):
    name = models.CharField(max_length=200)
    kind = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('devTools:detail', args=[self.id])
    