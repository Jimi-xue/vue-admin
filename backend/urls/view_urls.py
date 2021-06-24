from django.urls import path,include
from backend.views import *

urlpatterns = [
    path(r'add_book', add_book, ),
    path(r'show_books', show_books, ),
]