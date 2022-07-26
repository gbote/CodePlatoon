from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Genre(models.Model):
    type = models.CharField(max_length=255, unique=True)

# This model stores information about a book
class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    # The foreign  key is defined on the many side of the relationship
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    authors = models.ManyToManyField(Author, related_name='books')

# A library patron, akin to a user
class Patron(models.Model):
    name = models.CharField(max_length=255, unique=True)

# This model tracks each actual physical copy (or ebook, audiobook license) of a book.
# This model will let us see how many copies of a book we have, what kind
# each copy of the book is, and if the book is checked out or not (and if so by who)
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # A copy of a book does not have to be checked out
    checked_out_by = models.ForeignKey(Patron, null=True, on_delete=models.CASCADE)

    # TODO: Write a validator.
    # Valid types: 'paperback', 'hardcover', 'audiobook', 'ebook'
    type = models.CharField(max_length=255)
