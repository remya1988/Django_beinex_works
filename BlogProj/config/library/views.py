from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from .models import *
from . import forms
from django.contrib import messages
from django.shortcuts import redirect,render
from django.urls import reverse_lazy

# Create your views here.

# class based views
class ListBooks(ListView):
    model = Book
    context_object_name = 'book'
    template_name = 'book_list.html'

class ListAuthor(ListBooks):
    model = Author
    context_object_name = "auth"
    template_name = "author_list.html"

class BookDetails(DetailView):
    model = Book
    context_object_name = 'bk'
    template_name = 'book_details.html'
class CreateBook(CreateView):
    form_class = forms.AddBookForm
    model = Book
    template_name = 'add_book.html'
    success_url = reverse_lazy("book-list")

class UpdateBook(UpdateView):
    model = Book
    form_class = forms.EditBookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy("book-list")

def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Book.objects.get(id=id).delete()
    return redirect("book-list")


def home(request):
    return render(request,'home.html')
def book_list(request):
    books=["Book 1",
           "Book 2",
           "Book 3",
           "Book 4",
           "Book 5"]
    context ={
        "books":books
    }
    return render(request,'book_list.html',context)

def book_details(request,bookid):
    context={
        'bookid':bookid
    }
    return render(request,'book_details.html',context)