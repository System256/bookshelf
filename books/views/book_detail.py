from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
from books.models import Book


def get_book(book_id: int) -> Book | None:
    try:
        return Book.objects.get(id=book_id)
    except ObjectDoesNotExist:
        return None


def book_details_view(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_book(book_id)
    return render(request, 'book_detail.html', context={'book': book})


def book_details_api_view(request: HttpRequest, book_id: int) -> HttpResponse | JsonResponse:
    book = get_book(book_id)

    if book is None:
        return HttpResponseNotFound()

    return JsonResponse({
        'id': book.pk,
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description,
    })