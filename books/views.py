from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class BookListView(ListView):
    model = Book
    template_name = 'books/home.html'
    context_object_name = 'books'
    ordering = ['-date_added']

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'ISBN', 'publisher', 'genre', 'location', 'summary', 'available']
    template_name = 'books/book_add_form.html'
    context_object_name = 'form'


    def test_func(self):
        current_user= self.request.user
        if current_user.has_perm('books.add_book'):
            return True
        return False

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'ISBN', 'publisher', 'genre', 'location', 'summary', 'available']
    template_name = 'books/book_update_form.html'
    context_object_name = 'form'

    def test_func(self):
        current_user= self.request.user
        if current_user.has_perm('books.change_book'):
            return True
        return False

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_delete_confirm.html'
    context_object_name = 'book'
    success_url = '/library/'
    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.change_book'):
            return True
        return False

