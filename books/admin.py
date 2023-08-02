from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'text', 'datetime_created']
