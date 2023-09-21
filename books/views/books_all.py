from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from books.models import Book
    

def books_view(request: HttpRequest) -> HttpResponse:
    title = 'Спиcок всех книг'
    books = Book.objects.all()
    return render(request, 'books.html', context={'title': title, 'books': books})


def books_api_view(request: HttpRequest) -> JsonResponse:
    books = list(Book.objects.values())
    return JsonResponse(books, safe=False)