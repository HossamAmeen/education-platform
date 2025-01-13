from django.db import models


class Slider(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    ordering = models.IntegerField()
    link = models.URLField()
