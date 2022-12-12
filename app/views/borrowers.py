from app.models import Borrower
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpRequest
from app.forms.borrower_form import BorrowerForm

def index(request):
    borrowers = Borrower.objects.all()

    return render(
        request, 
        'app/borrowers/index.html',
        {
            'borrowers': borrowers
        }
    )

def edit(request, id) :
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0 :
            form = BorrowerForm()
        else :
            borrowers = Borrower.objects.get(pk = id)
            form = BorrowerForm(instance = borrowers)
        return render(
            request,
            'app/borrowers/edit.html',
            {
                'form' : form
            }
            )
    else:
        if id == 0 :
            form = BorrowerForm(request.POST)
        else :
            borrowers = Borrower.objects.get(pk = id)
            form = BorrowerForm(request.POST, instance = borrowers)
        if form.is_valid():
            form.save()
            messages.success(request,"Borrower has been modified successfully !")
        return redirect('borrowers/')


def delete(request, id):
    borrowers = Borrower.objects.get(pk = id)
    borrowers.delete()
    messages.success(request,"Borrower has been deletedd successfully !")
    return redirect('/borrowers')


def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET' :
        form = BorrowerForm
    return render(
        request,
        'app/borrowers/add.html',
        {
            'form' : form
        }
    )


def store(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Borrower has been saved successfully !")
        return redirect('/borrowers')
