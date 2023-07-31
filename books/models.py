from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()
    price = models.PositiveBigIntegerField()
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['-datetime_created']

    def __str__(self):
        return self.title
