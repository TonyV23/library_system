from django.shortcuts import redirect,render
from django.http import HttpRequest

from app.models import Author, Book, Borrow, Borrower, Category, Emplacement

def printAuthors(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Print All Authors'
    authors = Author.objects.all()
    return render(
        request,
        'app/prints/authors.html',
        {
            'authors' : authors,
            'page_title' : page_title
        }
    )

def printBooks(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Print All Books'
    books = Book.objects.all()
    return render(
        request,
        'app/prints/books.html',
        {
            'books': books,
            'page_title' : page_title
        }
    )

def printBorrowers(request):
    borrowers = Borrower.objects.all()
    page_title = 'Print All Borrowers'
    return render(
        request, 
        'app/prints/borrowers.html',
        {
            'borrowers': borrowers,
            'page_title' : page_title
        }
    )

def printBorrows(request):
    page_title = 'Print All Borrows'
    assert isinstance(request, HttpRequest)
    Borrows = Borrow.objects.all()
    return render(
        request,
        'app/prints/borrows.html',
        {
            'borrows': Borrows,
            'page_title' : page_title
        }
    )

def printCategories(request):
    page_title = 'Print All Categories'
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/prints/categories.html',
        {
            'categories': categories,
            'page_title' : page_title
        }
    )

def printEmplacements(request):
    page_title = 'Print All Emplacements'
    assert isinstance(request, HttpRequest)
    emplacements = Emplacement.objects.all()
    return render(
        request,
        'app/prints/emplacements.html',
        {
            'emplacements' : emplacements,
            'page_title' : page_title
        }
    )
def resume(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Print All'
    authors = Author.objects.all()
    books = Book.objects.all()
    borrowers = Borrower.objects.all()
    Borrows = Borrow.objects.all()
    categories = Category.objects.all()
    emplacements = Emplacement.objects.all()
    
    return render(
        request,
        'app/prints/resume.html',
        {
            'emplacements' : emplacements,
            'authors' : authors,
            'books': books,
            'borrowers': borrowers,
            'borrows': Borrows,
            'categories': categories,
            'page_title' : page_title
        }
    )