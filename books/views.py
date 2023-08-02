from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book
from .forms import CommentForm


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

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    context = {'book': book, 'comments': book_comments, 'comment_form': comment_form}
    return render(request, 'books/details_view.html', context)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'translator', 'content', 'price', 'cover']
    template_name = 'books/create_view.html'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'translator', 'content', 'price', 'cover']
    template_name = 'books/update_view.html'


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'books/delete_view.html'
    success_url = reverse_lazy('book:list_view')
