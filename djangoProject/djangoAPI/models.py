from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=100)