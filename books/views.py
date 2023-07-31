from django.views.generic import ListView, DetailView, CreateView

from .models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/list_view.html'
    context_object_name = 'books'


class BookDetailsView(DetailView):
    model = Book
    template_name = 'books/details_view.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'content', 'price']
    template_name = 'books/create_view.html'
