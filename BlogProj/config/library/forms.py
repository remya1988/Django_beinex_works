from django import forms
from .models import Book

class EditBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"

class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['book_title','book_author','summary']