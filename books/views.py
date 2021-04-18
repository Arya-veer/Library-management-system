from django.shortcuts import render
from .models import Book
def home(request):
    context = {
        'books': Book.objects.all(),
        'title' : 'Home',
    }
    return render(request, 'books/home.html', context)
