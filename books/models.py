from django.db import models
from django.urls import reverse
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    translator = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    price = models.PositiveBigIntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['-datetime_created']

    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse('book:details_view', args=[self.id])
