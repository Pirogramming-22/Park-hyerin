# Generated by Django 5.1.4 on 2025-01-10 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereview',
            name='genre',
            field=models.CharField(choices=[('action', '액션'), ('comedy', '코미디'), ('drama', '드라마'), ('horror', '공포'), ('fantasy', '판타지'), ('SF', '공상과학'), ('musical', '뮤지컬'), ('history', '역사'), ('mystery', '미스터리'), ('documentary', '다큐'), ('animation', '애니메이션')], max_length=50, verbose_name='장르'),
        ),
        migrations.AlterField(
            model_name='moviereview',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
