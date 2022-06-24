import email
from django.db import models
from email_validator import validate_email
from django.core.exceptions import ValidationError

# Create your models here.


class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=8)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    zip = models.CharField(max_length=20)
