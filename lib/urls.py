from django.urls import path
from . import views
app_name="lib"

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.book_list, name="book_list"),
    path('genres/', views.genre_list, name="genre_list"),
    path('authors/', views.author_list, name="author_list"),
    path('book/<int:pk>/', views.book_detail, name="book_detail"),
    path('genre/<int:pk>/', views.genre_detail, name="genre_detail"),
    path('author/<int:pk>/', views.author_detail, name="author_detail"),
#http://127.0.0.1:8000/lib/api/books/all/
    path('api/books/all', views.BookListAPIView.as_view(), name="api_book_list"),
#http://127.0.0.1:8000/lib/api/author/1/
    path('api/author/<int:pk>', views.AuthorDetailAPIView.as_view(), name="api_author_list"),
]
