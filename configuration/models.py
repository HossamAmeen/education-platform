from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Slider(models.Model):
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/')
    ordering = models.IntegerField()
    link = models.URLField(null=True)


class Review(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    rate = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(5)])
    ordering = models.IntegerField()
