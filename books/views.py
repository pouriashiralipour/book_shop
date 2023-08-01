from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/list_view.html'
    context_object_name = 'books'


class BookDetailsView(DetailView):
    model = Book
    template_name = 'books/details_view.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'translator', 'content', 'price', 'cover']
    template_name = 'books/create_view.html'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'translator', 'content', 'price', 'cover']
    template_name = 'books/update_view.html'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete_view.html'
    success_url = reverse_lazy('book:list_view')
