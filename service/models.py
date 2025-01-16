from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    add=models.TextField()

class Bookinfo(models.Model):
    bookname=models.CharField(max_length=50)
    sem_year=models.TextField()
    link=models.URLField()

