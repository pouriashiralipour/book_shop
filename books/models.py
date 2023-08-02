from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.translation import gettext, gettext_lazy as _


class Book(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'))
    title = models.CharField(max_length=200, verbose_name=_('title'))
    author = models.CharField(max_length=200, verbose_name=_('author'))
    translator = models.CharField(max_length=200, blank=True, verbose_name=_('translator'))
    content = models.TextField(verbose_name=_('content'))
    price = models.PositiveBigIntegerField(verbose_name=_('price'))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_('cover'))
    datetime_created = models.DateTimeField(default=timezone.now, verbose_name=_('datetime_created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('datetime_modified'))

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['-datetime_created']

    def __str__(self):
        return f'{self.author}: {self.title}'

    def get_absolute_url(self):
        return reverse('book:details_view', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'))
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name=_('book'))
    text = models.TextField(verbose_name=_('text'))
    is_active = models.BooleanField(default=True, verbose_name=_('is_active'))
    recommend = models.BooleanField(default=True, verbose_name=_('recommend'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('datetime_created'))

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-datetime_created']

    def __str__(self):
        return f'{self.user}: {self.text}'



