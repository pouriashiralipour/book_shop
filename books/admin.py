from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class BookAdmin(admin.ModelAdmin):
    pass
