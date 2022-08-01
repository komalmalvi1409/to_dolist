from django.db import models
from django.db.models import Model
from datetime import datetime 
from django.urls import reverse


class Login(models.Model):
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=50)


class To_doo(models.Model):
    title =models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=50)
    duedate=models.DateTimeField(default=datetime.now(), blank=True)
    