from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from .utils import get_book


def book_details_view(request: HttpRequest, book_id: int) -> HttpResponse:
    book = get_book(book_id)
    return render(request, 'book_detail.html', context={'book': book, 'book_id': book_id})


def book_details_api_view(request: HttpRequest, book_id: int) -> JsonResponse:
    book = get_book(book_id)

    if book is None:
        return JsonResponse({'error': f'Книга по ID {book_id} не найдена'})

    return JsonResponse({
        'id': book.pk,
        'title': book.title,
        'author_full_name': book.author_full_name,
        'year_of_publishing': book.year_of_publishing,
        'copies_printed': book.copies_printed,
        'short_description': book.short_description,
    })