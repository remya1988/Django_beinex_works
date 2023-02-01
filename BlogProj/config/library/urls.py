from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name="home"),
    path('book-list/',ListBooks.as_view(),name="book-list"),
    path('author-list/',ListAuthor.as_view(),name="author-list"),
    path('book/<int:pk>/detail/',BookDetails.as_view(),name="book-detail"),
    path('book/edit/<int:pk>/',UpdateBook.as_view(),name="edit-book"),
    path('book/add/',CreateBook.as_view(),name="add-book"),
    path('book/delete/<int:id>/',delete_book,name="delete-book")
]