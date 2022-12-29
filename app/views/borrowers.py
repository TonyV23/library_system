from app.models import Borrower
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from app.forms.borrower_form import BorrowerForm

def index(request):
    borrowers = Borrower.objects.all()
    page_title = 'All Borrowers'
    return render(
        request, 
        'app/borrowers/index.html',
        {
            'borrowers': borrowers,
            'page_title' : page_title 
        }
    )


def add(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Add Borrower'
    if request.method == 'GET' :
        form = BorrowerForm
    return render(
        request,
        'app/borrowers/add.html',
        {
            'form' : form,
            'page_title' : page_title
            
        }
    )


def store(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Borrower has been saved successfully !")
        else :
            messages.success(request, form.errors)
        return redirect('/borrowers')


def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = BorrowerForm(request.POST)
        else:
            borrower = Borrower.objects.get(pk=id)
            form = BorrowerForm(request.POST, instance=borrower)
        if form.is_valid():
            form.save()
        messages.success(request, "Borrower has been updated successfully !")
        return redirect('/borrowers')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Edit Borrower'
    if request.method == 'GET':
        if id == 0:
            form = BorrowerForm()
        else:
            borrower = Borrower.objects.get(pk=id)
            form = BorrowerForm(instance=borrower)
        return render(
            request,
            'app/borrowers/edit.html',
            {
                'form': form,
                'page_title' : page_title
            }
        )

def delete(request, id):
    borrowers = Borrower.objects.get(pk = id)
    borrowers.delete()
    messages.success(request,"Borrower has been deleted successfully !")
    return redirect('/borrowers')