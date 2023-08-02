from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render

from .models import Book


class BookListView(ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/list_view.html'
    context_object_name = 'books'


# class BookDetailsView(DetailView):
#     model = Book
#     template_name = 'books/details_view.html'
def book_details_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comments = book.comments.all()
    return render(request, 'books/details_view.html', {'book': book, 'comments': book_comments})


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
