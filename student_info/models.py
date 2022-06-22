from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
