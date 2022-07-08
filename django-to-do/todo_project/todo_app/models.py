from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # we're using email to identify the user and log them in
    USERNAME_FIELD = 'email'

    # email & password are required by default
    REQUIRED_FIELDS = []



class Todo_Items(models.Model):
    contents = models.TextField()
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="todo_items")

    def __str__(self):
        return f"{self.contents}"