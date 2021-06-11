from django.contrib.auth.views import LogoutView
from django.urls import path

from core.views.auth import LoginView, RegisterView
from core.views.author import AuthorsView, AuthorDetailView, AuthorCreateView, AuthorDeleteView
from core.views.books import DetailBookView, BookCreateView, BookDeleteView
from core.views.genres import GenreCreateView
from core.views.base import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('book/<int:pk>', DetailBookView.as_view(), name='detail_book'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('author/<int:pk>', AuthorDetailView.as_view(), name='detail_author'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='author_delete'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create')
]