from django import forms
from backend.models import Book

class BookForm(forms.ModelForm):
    book_name = forms.CharField(label="书名")

    class Meta:
         model=Book
         fields=('book_name',)