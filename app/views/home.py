from django.http import HttpRequest
from django.shortcuts import render
from app.models import Author, Book, Borrow, Borrower
from datetime import datetime

def index(request):
    count_authors = Author.objects.all().count()
    count_books = Book.objects.all().count()
    count_borrows = Borrow.objects.all().count()
    count_borrowers = Borrower.objects.all().count()
    time= datetime.now()
    
    return render(
        request,
        'app/home/index.html',
        {
            'count_authors' :count_authors,
            'count_books' :count_books,
            'count_borrows' :count_borrows,
            'count_borrowers' :count_borrowers,
            'time' :time
        }           
        
    )