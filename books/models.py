from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Author(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    publisher = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    location = models.TextField()
    available = models.BooleanField(default=True)
    ISBN = models.CharField(max_length=17, default='000-000-000-000-0')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})