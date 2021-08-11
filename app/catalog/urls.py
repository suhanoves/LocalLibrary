from django.urls import path

from catalog.views import *

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('books/', BooksView.as_view(), name='books'),
    path('authors/', AuthorsView.as_view(), name='authors'),
    path('book/<int:pk>', BookView.as_view(), name='book'),
    path('author/<int:pk>', AuthorView.as_view(), name='author'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('borrowed/', BorrowedBooks.as_view(), name='borrowed_books'),
    path('book/<uuid:pk>/renew/', renew_book_librarian, name='renew-book-librarian'),
    path('author/create', AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update', AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete', AuthorDelete.as_view(), name='author_delete'),
]
