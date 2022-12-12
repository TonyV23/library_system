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
            authors = Borrower.objects.get(pk = id)
            form = BorrowerForm(instance = authors)
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
            authors = Borrower.objects.get(pk = id)
            form = BorrowerForm(request.POST, instance = authors)
        if form.is_valid():
            form.save()
            messages.success(request,"Author has been modified successfully !")
        return redirect('/borrowers')


def delete(request, id):
    authors = Borrower.objects.get(pk = id)
    authors.delete()
    print('deleted borrower...')
    messages.success(request,"Borrower has been deletedd successfully !")
    return redirect('/borrowers')