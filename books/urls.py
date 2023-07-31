from django.urls import path

from .views import ListView

urlpatterns = [
    path('', ListView.as_view(), name='book_list_view'),
]
