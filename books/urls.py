from django.urls import path

from .views import BookListView, BookDetailsView, BookCreateView, BookUpdateView, BookDeleteView

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='list_view'),
    path('<int:pk>/', BookDetailsView.as_view(), name='details_view'),
    path('new/', BookCreateView.as_view(), name='create_view'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='update_view')
]
