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
    
    get_all_authors_names = Author.objects.values('first_name')
    get_all_authors_names_list=[]
    
    for i in range(0, len(get_all_authors_names)):
        get_all_authors_names_list.append(list(get_all_authors_names[i].values())[0])
    

    author_book_dict = getAllAuthorsOccurrence()
    
    return render(
        request,
        'app/home/index.html',
        {
            'count_authors' :count_authors,
            'count_books' :count_books,
            'count_borrows' :count_borrows,
            'count_borrowers' :count_borrowers,
            'time' :time,
            'get_all_authors_names_list' : get_all_authors_names_list,
            'author_book_dict' : author_book_dict.values(),
            
        }           
        
    )

def getAllAuthorsOccurrence():
    get_all_authors_ids = Author.objects.values('id')
    get_all_authors_ids_list=[]
    
    for i in range(0, len(get_all_authors_ids)):
        get_all_authors_ids_list.append(list(get_all_authors_ids[i].values())[0])
    
    get_all_books_author_ids = Book.objects.values('author_id')
    get_all_books_author_ids_list =[]

    for i in range(0, len(get_all_books_author_ids)):
        get_all_books_author_ids_list.append(list(get_all_books_author_ids[i].values())[0])

    author_book_dict = {}
    for i in range(0, len(get_all_authors_ids_list)) :
        occurrence_authors = 0
        if get_all_authors_ids_list[i] in get_all_books_author_ids_list :
            for j in range(0, len(get_all_books_author_ids_list)):
                if get_all_authors_ids_list[i] == get_all_books_author_ids_list[j]:
                    occurrence_authors = occurrence_authors + 1
            author_book_dict [get_all_authors_ids_list[i]] = occurrence_authors
    
    return author_book_dict