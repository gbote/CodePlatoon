from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Genre(models.Model):
    type = models.CharField(max_length=255, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    # The foreign  key is defined on the many side of the relationship
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    authors = models.ManyToManyField(Author, related_name='books')

