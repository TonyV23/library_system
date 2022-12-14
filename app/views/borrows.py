from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Borrow,Category,Book
from app.forms import BorrowForm
from django.contrib import messages

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    Borrows = Borrow.objects.all()
    return render(
        request,
        'app/borrows/index.html',
        {
            'Borrows': Borrows
        }
    )

def add(request):
    assert isinstance(request, HttpRequest)
    categories = Category.objects.all()
    form = BorrowForm()
    return render(
        request,
        'app/borrows/add.html',
        {
            'form': form,
            'categories':categories
        }
    )

def store(request):
    if request.method == 'POST':
        form = BorrowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Borrow has been saved successfully ! ")
        else:
            messages.success(request,form.errors)
        return redirect('/borrows')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = BorrowForm()
        else:
            Borrows = Borrow.objects.get(pk = id)
            form = BorrowForm(instance = Borrows)
        return render(
            request,
            'app/borrows/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = BorrowForm(request.POST)
        else:
            Borrows = Borrow.objects.get(pk=id)
            form = BorrowForm(request.POST,instance = Borrows)
        if form.is_valid():
            form.save()
            messages.success(request,"Borrow has been modified successfully !")
        return redirect('/borrows')
    
def delete(request, id):
    Borrows = Borrow.objects.get(pk=id)
    Borrows.delete()
    messages.success(request,"Borrow has been deleted successfully !")
    return redirect('/borrows')

def getBooks(request):
    category_id = request.GET.get('category_id')
    books = Book.objects.filter(category_id = category_id).order_by('book_title')
    return render(
        request,
        'app/borrows/getBooks.html',
        {
            'books': books
        }
    )