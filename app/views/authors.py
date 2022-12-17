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


def edit(request, id):
    assert isinstance(request, HttpRequest)
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
                'form': form
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
