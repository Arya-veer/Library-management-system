from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:pk>/', views.RequestCreateView.as_view(), name='book-request'),
    path('requestList/', views.RequestListView.as_view(), name='request-list'),
    path('<int:pk>/decline/', views.RequestDeclineView.as_view(), name='request-decline'),
    path('<int:pk>/approve', views.RequestApproveView.as_view(), name='request-approve'),
]