

from django.urls  import path,include
from .views import BookListAPIView as BookList, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')



urlpatterns = [
    # Maps to the BookList view 
    # http://127.0.0.1:8000/api/books/
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]
#routers endpoints
# GET /api/books/ - List all books (list action)
# POST /api/books/ - Create a new book (create action)
# GET /api/books/{id}/ - Retrieve a book by ID (retrieve action)
# PUT /api/books/{id}/ - Update a book by ID (update action)
# DELETE /api/books/{id}/ - Delete a book by ID (destroy action)
