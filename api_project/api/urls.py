

from django.urls  import path
from .views import BookListAPIView as BookList

urlpatterns = [
    # Maps to the BookList view 
    # http://127.0.0.1:8000/api/books/
    path('books/', BookList.as_view(), name='book-list'),  
]