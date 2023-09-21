from django.contrib import admin
from django.urls import path

from books.views.books_all import books_view, books_api_view
from books.views.book_detail import book_details_view, book_details_api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view),
    path('books/<int:book_id>/', book_details_view),
    path('api/books/', books_api_view),
    path('api/books/<int:book_id>/', book_details_api_view),
]