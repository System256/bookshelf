from django.shortcuts import get_object_or_404
from books.models import Book


def get_book(book_id: int) -> Book | None:
    return get_object_or_404(Book, pk=book_id)