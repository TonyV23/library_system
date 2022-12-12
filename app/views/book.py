from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Book
from app.forms import BookForm

def index(request):
    assert isinstance(request, HttpRequest)
    books = Book.objects.all()
    return render(
        request,
        'app/books/index.html',
        {
            'books': books
        }
    )
    
def add(request):
    form = BookForm()
    return render(
        request, 
        'app/books/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Book has been saved successfully !")
        return redirect('/books')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = BookForm()
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(instance=book)
        return render(
            request,
            'app/books/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = BookForm(request.POST)
        else:
            book = Book.objects.get(pk=id)
            form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        messages.success(request, "Book has been updated successfully !")
        return redirect('/books')
    
def delete(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    messages.success(request, "Book has been removed successfully !")
    return redirect('/books')