from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class AppUser(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    # this tells django that we'll be using the 'email' column to indentify users, instead of 'username'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 