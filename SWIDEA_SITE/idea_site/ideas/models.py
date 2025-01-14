from django.db import models
from devTools.models import DevTool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('아이디어명', max_length=200)
    image = models.ImageField('Image', upload_to='posts/%Y%m%d', blank=True)
    content = models.TextField('아이디어 설명')
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE)
    is_starred = models.BooleanField(default=False)

    def __str__(self):
        return self.title
