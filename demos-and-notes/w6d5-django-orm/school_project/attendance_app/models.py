from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    favorite_color = models.CharField(max_length=198, null=True)

class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Administrator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    

class Correct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)