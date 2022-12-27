from django.shortcuts import redirect,render
from django.http import HttpRequest

from app.models import Author, Book, Borrow, Borrower, Category, Emplacement

def printAuthors(request):
    assert isinstance(request, HttpRequest)
    authors = Author.objects.all()
    return render(
        request,
        'app/prints/authors.html',
        {
            'authors' : authors
        }
    )

def printBooks(request):
    assert isinstance(request, HttpRequest)
    books = Book.objects.all()
    return render(
        request,
        'app/prints/books.html',
        {
            'books': books
        }
    )

def printBorrowers(request):
    borrowers = Borrower.objects.all()

    return render(
        request, 
        'app/prints/borrowers.html',
        {
            'borrowers': borrowers
        }
    )

def printBorrows(request):
    assert isinstance(request, HttpRequest)
    Borrows = Borrow.objects.all()
    return render(
        request,
        'app/prints/borrows.html',
        {
            'borrows': Borrows
        }
    )

def printCategories(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/prints/categories.html',
        {
            'categories': categories
        }
    )

def printEmplacements(request):
    assert isinstance(request, HttpRequest)
    emplacements = Emplacement.objects.all()
    return render(
        request,
        'app/prints/emplacements.html',
        {
            'emplacements' : emplacements
        }
    )
def resume(request):
    assert isinstance(request, HttpRequest)
    
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
            'categories': categories
        }
    )