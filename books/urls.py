from django.urls import path

from .views import BookListView,  BookCreateView, BookUpdateView, BookDeleteView, book_details_view

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='list_view'),
    path('<int:pk>/', book_details_view, name='details_view'),
    path('new/', BookCreateView.as_view(), name='create_view'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete_view'),
]
