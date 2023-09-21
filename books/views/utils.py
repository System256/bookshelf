from django.core.exceptions import ObjectDoesNotExist
from books.models import Book


def get_book(book_id: int) -> Book | None:
    try:
        return Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        return None