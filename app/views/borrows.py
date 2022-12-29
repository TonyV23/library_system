from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Borrow,Category,Book,Borrow
from app.forms import BorrowForm
from django.contrib import messages

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    page_title = 'All Borrows'
    Borrows = Borrow.objects.all()
    return render(
        request,
        'app/borrows/index.html',
        {
            'borrows': Borrows,
            'page_title' : page_title
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    page_title = 'Add Borrow'
    categories = Category.objects.all()
    form = BorrowForm()
    return render(
        request,
        'app/borrows/add.html',
        {
            'form': form,
            'categories':categories,
            'page_title' : page_title
        }
    )

def store(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        book_id = form['book'].value()
        quantite_exemplaire = getBookExemplaire(book_id)
        if form.is_valid():
            if quantite_exemplaire <= 0 :
                messages.success(request," Book exemplaire insufficient ! ")
                
            elif form.cleaned_data['borrow_starting_date'] == form.cleaned_data['borrow_ending_date'] :
                messages.success(request," Incorrect Timeline ! ")
                
            elif form.cleaned_data['borrow_starting_date'] >= form.cleaned_data['borrow_ending_date'] :
                messages.success(request," Incorrect Timeline ! ")
            else :
                form.save()
                quantite_exemplaire = quantite_exemplaire - 1
                Book.objects.filter(id=book_id).update(exemplaire = quantite_exemplaire)
                messages.success(request," Borrow has been saved successfully ! ")
        else:
            messages.success(request,form.errors)
        return redirect('/borrows')

def update(request, id):
    if request.method == 'POST':
        if id == 0:
            form = BorrowForm(request.POST)
        else:
            borrow = Borrow.objects.get(pk=id)
            form = BorrowForm(request.POST, instance=borrow)
        if form.is_valid():
            form.save()
        messages.success(request, "Borrow has been updated successfully !")
        return redirect('/borrows')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    page_title = 'Edit Borrow'
    if request.method == 'GET':
        if id == 0:
            form = BorrowForm()
        else:
            borrow = Borrow.objects.get(pk=id)
            form = BorrowForm(instance=borrow)
        return render(
            request,
            'app/borrows/edit.html',
            {
                'form': form,
                'page_title': page_title
            }
        )

def delete(request, id):
    Borrows = Borrow.objects.get(pk=id)
    book_id = list(Borrow.objects.filter(id = id).values('book_id'))[0]['book_id']
    quantite_exemplaire = getBookExemplaire(book_id)
    quantite_exemplaire = quantite_exemplaire + 1
    Book.objects.filter(id = book_id).update(exemplaire = quantite_exemplaire)
    Borrows.delete()
    messages.success(request,"Borrow has been deleted successfully !")
    return redirect('/borrows')

def getBooks(request):
    page_title = 'Get book'
    category_id = request.GET.get('category_id')
    books = Book.objects.filter(category_id = category_id).order_by('book_title')
    return render(
        request,
        'app/borrows/getBooks.html',
        {
            'books': books
        }
    )
    
def getBookExemplaire(book_id):
   exemplaire = list(Book.objects.filter(id=book_id).values('exemplaire'))[0]['exemplaire']
   return exemplaire