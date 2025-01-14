from django.db import models


class Slider(models.Model):
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/')
    ordering = models.IntegerField()
    link = models.URLField(null=True)
