from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages

from app.models import Category
from app.forms import CategoryForm

def index(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'categories': categories
        }
    )
    
def add(request):
    form = CategoryForm()
    return render(
        request, 
        'app/categories/add.html',
        {
            'form': form
        }
    )
    
def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, "Category has been saved successfully !")
        return redirect('/categories')
    
def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(instance=category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            }
        )
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            category = Category.objects.get(pk=id)
            form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        messages.success(request, "Category has been updated successfully !")
        return redirect('/categories')
    
def delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    messages.success(request, "Category has been removed successfully !")
    return redirect('/categories')