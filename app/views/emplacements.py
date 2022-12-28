from django.http import HttpRequest
from django.shortcuts import redirect, render
from app.models import Emplacement
from app.forms import EmplacementForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    emplacements = Emplacement.objects.all()
    return render(
        request,
        'app/emplacements/index.html',
        {
            'emplacements' : emplacements
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET' :
        form = EmplacementForm
    return render(
        request,
        'app/emplacements/add.html',
        {
            'form' : form
        }
    )

def store(request):
    if request.method == 'POST':
        form = EmplacementForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['rank'] <= 0 :
                messages.success(request,"Rank Invalid !")
            else :
                form.save()
                messages.success(request,"Emplacement has been saved successfully !")
        else :
            messages.success(request, form.errors)
        return redirect('/emplacements')


def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == 'GET':
        if id == 0:
            form = EmplacementForm()
        else:
            emplacement = Emplacement.objects.get(pk=id)
            form = EmplacementForm(instance=emplacement)
        return render(
            request,
            'app/emplacements/edit.html',
            {
                'form': form
            }
        )

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = EmplacementForm(request.POST)
        else:
            emplacement = Emplacement.objects.get(pk=id)
            form = EmplacementForm(request.POST, instance=emplacement)
        if form.is_valid():
            if form.cleaned_data['rank'] <= 0 :
                messages.success(request,"Rank Invalid !")
            else :
                form.save()
                messages.success(request, "Emplacement has been updated successfully !")
        return redirect('/emplacements')

def delete(request, id):
    authors = Emplacement.objects.get(pk = id)
    authors.delete()
    messages.success(request,"Emplacement has been deleted successfully !")
    return redirect('/emplacements')
