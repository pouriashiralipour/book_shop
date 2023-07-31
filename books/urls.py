from django.urls import path

from .views import BookListView, BookDetailsView

app_name = 'book'

urlpatterns = [
    path('', BookListView.as_view(), name='list_view'),
    path('<int:pk>/', BookDetailsView.as_view(), name='details_view'),
]
