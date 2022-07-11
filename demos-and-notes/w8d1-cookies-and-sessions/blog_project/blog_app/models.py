from django.db import models

# Create your models here.

class AppUser(models.Model):
    user_name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=99)