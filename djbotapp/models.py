import django
from django.db import models
import sys
from django.conf import settings

# Create your models here.


class Request(models.Model):
    userId = models.TextField()
    request = models.TextField()


class Movie(models.Model):
    Name = models.TextField()
    Link = models.TextField()
    Status = models.BooleanField()
    request = models.ForeignKey('Request', on_delete=models.CASCADE)


class User(models.Model):
    user = models.TextField()
    userLanguage = models.TextField()
    request = models.ForeignKey('Request', on_delete=models.CASCADE)
