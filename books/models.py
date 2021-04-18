from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    publisher = models.CharField(max_length=100)
    summary = models.TextField(blank=True)
    location = models.TextField()
    available = models.BooleanField(default=True)


def __str__(self):
    return self.title


