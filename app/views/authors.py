from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Author
from app.forms import AuthorForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    authors = Author.objects.all()
    return render(
        request,
        'app/authors/index.html',
        {
            'authors' : authors
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET' :
        form = AuthorForm
    return render(
        request,
        'app/authors/add.html',
        {
            'form' : form
        }
    )

def store(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Author has been saved successfully !")
        return redirect('/authors')

def edit(request, id) :
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0 :
            form = AuthorForm()
        else :
            authors = Author.objects.get(pk = id)
            form = AuthorForm(instance = authors)
        return render(
            request,
            'app/authors/edit.html',
            {
                'form' : form
            }
            )
    else:
        if id == 0 :
            form = AuthorForm(request.POST)
        else :
            authors = Author.objects.get(pk = id)
            form = AuthorForm(request.POST, instance = authors)
        if form.is_valid():
            form.save()
            messages.success(request,"Author has been modified successfully !")
        return redirect('/authors')

def delete(request, id):
    authors = Author.objects.get(pk = id)
    authors.delete()
    messages.success(request,"Author has been deletedd successfully !")
    return redirect('/authors')