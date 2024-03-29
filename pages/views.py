from django.views.generic import ListView

from books.models import Book


class HomePageView(ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/list_view.html'
    context_object_name = 'books'
