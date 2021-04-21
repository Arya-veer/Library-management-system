from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from django.urls import reverse
from django.utils import timezone
import datetime

class request_detail(models.Model):
    book_detail = models.ForeignKey(Book, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    return_date = models.DateField(default=timezone.now()+datetime.timedelta(days=7))
    request_status = models.CharField(max_length=15, default = 'Pending')
    confirm_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.book_detail.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.book_detail.pk})