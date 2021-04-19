from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='books-home'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('book/new/', views.BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete')
]