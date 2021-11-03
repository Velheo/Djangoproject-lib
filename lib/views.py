from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import *
from .serializers import *
def look_ups():
    #print('#1')
    author1=Author.objects.get(first__iexact='jane')
    #print(author1)
def index(request):
    look_ups()
    n_books=Book.objects.all().count()
    n_authors = Author.objects.all().count()
    n_genres = Genre.objects.all().count()
    n_av_instances=BookInstance.objects.filter(status__exact='a').count()
    context={
        'n_books': n_books,
        'n_authors': n_authors,
        'n_genres': n_genres,
        'n_av_instances': n_av_instances,
    }
    #return HttpResponse('<h1>Local Library</h1>')
    return render(request, 'lib/index.html', context)
def book_list(request):
    context={
        'books': Book.objects.all(),
    }
    return render(request, 'lib/book_list.html', context)
def genre_list(request):
    context={
        'genres': Genre.objects.all(),
    }
    return render(request, 'lib/genre_list.html', context)

def author_list(request):
    context={
        'authors': Author.objects.all(),
    }
    return render(request, 'lib/author_list.html', context)
def book_detail(request, pk):
    context={
        'book': Book.objects.get(pk=pk),
    }
    return render(request, 'lib/book_detail.html', context)
def genre_detail(request, pk):
    context={
        'genre': Genre.objects.get(pk=pk),
    }
    return render(request, 'lib/genre_detail.html', context)
def author_detail(request, pk):
    context={
        'author': Author.objects.get(id__exact=pk),
    }
    #print(context['author'].get_genres())
    return render(request, 'lib/author_detail.html', context)

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer1

class AuthorDetailAPIView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer1