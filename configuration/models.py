from django.db import models


class Slider(models.Model):
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='media/')
    ordering = models.IntegerField()
    link = models.URLField(null=True)


class Configuration(models.Model):
    phone_number_1 = models.CharField(max_length=50)
    phone_number_2 = models.CharField(max_length=50)
    adderss_1 = models.CharField(max_length=100)
    adderss_2 = models.CharField(max_length=100)
    email = models.EmailField()
    about_us = models.TextField()
    our_vision = models.TextField()
    our_mission = models.TextField()
