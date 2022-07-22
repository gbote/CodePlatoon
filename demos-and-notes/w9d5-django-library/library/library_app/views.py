from django.shortcuts import render
from .models import Author, Genre, Book

# Create your views here.
def list_genres(request):
    all_genres = Genre.objects.all().values
    return render(request, 'pages/list_genres.html', { "all_genres": all_genres })

def list_author_books(request, authorid):
    author = Author.objects.get(id=authorid)
    all_books = author.books.objects.all()
    return render(request, 'pages/list_author_books.html', { "author_name": author.name, "all_books": all_books })


# New author
# Existing genre
def new_book_author(request, author_name, book_name, genre_name):
    # get the genre name
    # select * from genre where genre.type=genre_name
    genre = Genre.objects.get(type=genre_name)

    new_author = Author(name=author_name)
    new_author.full_clean()
    new_author.save()

    new_book = Book(author=new_author, genre=genre)
    new_book.full_clean()
    new_book.save()

