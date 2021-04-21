from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from books.models import Book
from .forms import RequestPeriodForm
from .models import request_detail


class RequestCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = request_detail
    form_class = RequestPeriodForm
    template_name = 'borrows/request_book.html'
    context_object_name = 'form'


    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.add_book'):
            return False
        return True

    def form_valid(self, form):
        current_book = Book.objects.get(id=self.kwargs.get('pk'))
        form.instance.requested_by = self.request.user
        form.instance.book_detail = current_book
        return super().form_valid(form)

class RequestListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = request_detail
    template_name = 'borrows/requests_list.html'
    context_object_name = 'requests'
    ordering = ['book_detail']

    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.add_book'):
            return True
        return False

class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = User
    template_name = 'borrows/profile_for_lib.html'
    context_object_name = 'user'

    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.add_book'):
            return True
        return False


class RequestDeclineView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = request_detail
    template_name = 'borrows/post_delete.html'
    context_object_name = 'form'
    fields = ['confirm_delete']

    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.change_book'):
            return True
        return False

    def form_valid(self, form):
        if(form.instance.confirm_delete==True):
            form.instance.request_status = 'Declined'
        return super().form_valid(form)

class RequestApproveView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = request_detail
    template_name = 'borrows/request_approve.html'
    context_object_name = 'form'
    form_class = RequestPeriodForm

    def test_func(self):
        current_user = self.request.user
        if current_user.has_perm('books.change_book'):
            return True
        return False

    def form_valid(self, form):
        form.instance.request_status = 'Borrowed'
        form.instance.book_detail.available = False
        return super().form_valid(form)

# def RequestDeclineView(request):
#
#
#     def test_func(self):
#         current_user = self.request.user
#         if current_user.has_perm('books.change_book'):
#             current_request = request_detail.objects.get(id=self.kwargs.get('pk'))
#             current_request.request_status = 'Declined'
#             return redirect('request-list')
#
#     test_func()