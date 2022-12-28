from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Author, Book
from app.forms import AuthorForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'All Authors'
    authors = Author.objects.all()
    return render(
        request,
        'app/authors/index.html',
        {
            'authors' : authors,
            'page_title' :page_title
        }
    )
    
def details(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Details Author'
    if request.method == 'GET':
        count_books = Book.objects.filter(author_id=id).values().all().count()
        books = Book.objects.filter(author_id=id).all()
        author = Author.objects.get(pk=id)
        return render(
            request,
            'app/authors/details.html',
            {
                'count_books' :count_books,
                'books' :books,
                'author': author,
                'page_title' : page_title
            }
        )

def add(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Add Author'
    if request.method == 'GET' :
        form = AuthorForm
    return render(
        request,
        'app/authors/add.html',
        {
            'form' : form,
            'page_title' :page_title
        }
    )

def store(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Author has been saved successfully !")
        else :
            messages.success(request, form.errors)
        return redirect('/authors')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Edit Author'
    if request.method == 'GET':
        if id == 0:
            form = AuthorForm()
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(instance=author)
        return render(
            request,
            'app/authors/edit.html',
            {
                'form': form,
                'page_title' :page_title
            }
        )

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = AuthorForm(request.POST)
        else:
            author = Author.objects.get(pk=id)
            form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
        messages.success(request, "Author has been updated successfully !")
        return redirect('/authors')

def delete(request, id):
    authors = Author.objects.get(pk = id)
    authors.delete()
    messages.success(request,"Author has been deleted successfully !")
    return redirect('/authors')
