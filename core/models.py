from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.aggregates import Max

class User(AbstractUser):
    pass

class Chryon(models.Model):
    date = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
