

from django.urls  import path
from .views import BookListAPIView

urlpatterns = [
    # Maps to the BookList view 
    # http://127.0.0.1:8000/api/books/
    path('books/', BookListAPIView.as_view(), name='book-list'),  
]