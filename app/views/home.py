from django.http import HttpRequest
from django.shortcuts import render
from app.models import Author, Book, Borrow, Borrower, Category
from datetime import datetime

from django.db.models import Count


def index(request):
    count_authors = Author.objects.all().count()
    count_books = Book.objects.all().count()
    count_borrows = Borrow.objects.all().count()
    count_borrowers = Borrower.objects.all().count()
    time= datetime.now()
    
    get_all_authors_names = Author.objects.values('first_name')
    get_all_authors_names_list = []
    
    for i in range(0, len(get_all_authors_names)):
        get_all_authors_names_list.append(list(get_all_authors_names[i].values())[0])
    
    
    get_all_books_categories_name = Category.objects.values('category_name')
    get_all_books_categories_name_list = []

    for k in range(0, len(get_all_books_categories_name)):
        get_all_books_categories_name_list.append(list(get_all_books_categories_name[k].values())[0])

    author_book_dict = getAllAuthorsOccurrence()
    category_book_dict = getAllCategoriesOccurrence()

    # for principal chart 
    books_borrowed_per_day = Borrow.objects.extra(select={'day': 'date( borrow_starting_date )'}).values('day').annotate(available=Count('borrow_starting_date'))
    books_borrowed_per_year = Borrow.objects.extra(select={'year':"EXTRACT(year FROM borrow_starting_date)"}).values('year').annotate(Count('pk')) 
    books_borrowed_per_month = Borrow.objects.extra(select={'month':"EXTRACT(month FROM borrow_starting_date)"}).values('month').annotate(Count('pk'))

    page_title = 'Home'

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
            'get_all_books_categories_name_list' : get_all_books_categories_name_list,
            'category_book_dict' : category_book_dict.values(),

            'books_borrowed_per_day' : books_borrowed_per_day, 
            'books_borrowed_per_year' : books_borrowed_per_year, 
            'books_borrowed_per_month' : books_borrowed_per_month,

            'page_title' : page_title 

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


def getAllCategoriesOccurrence():
    get_all_category_name_ids = Category.objects.values('id')
    get_all_category_name_ids_list=[]

    for i in range(0, len(get_all_category_name_ids)):
        get_all_category_name_ids_list.append(list(get_all_category_name_ids[i].values())[0])

    get_all_books_category_ids = Book.objects.values('category_id')
    get_all_books_category_ids_list =[]

    for k in range(0, len(get_all_books_category_ids)):
        get_all_books_category_ids_list.append(list(get_all_books_category_ids[k].values())[0])

    category_book_dict = {}

    for i in range(0, len(get_all_category_name_ids_list)):
        occurrence_category = 0
        if get_all_category_name_ids_list[i] in get_all_books_category_ids_list :
            for j in range (0, len(get_all_books_category_ids_list)):
                if get_all_category_name_ids_list[i] == get_all_books_category_ids_list[j] :
                    occurrence_category = occurrence_category + 1
            category_book_dict[get_all_category_name_ids_list[i]] = occurrence_category
    
    return category_book_dict

