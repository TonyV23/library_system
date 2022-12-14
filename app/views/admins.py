from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from app.forms import AdminForm

def index(request):
    admins = User.objects.all()
    return render(
        request,
        'app/admins/index.html',
        {
            'admins': admins
        }
    )
    

def register(request):
    form = AdminForm()
    return render(
        request, 
        'app/admins/register.html',
        {
            'form': form
        }
    )


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        admin = authenticate(request, username=username, password=password)
        if admin is not None:
            login(request, admin)
            return redirect('/home')
        else:
            messages.info(request, 'Username or password incorrect')
            
    return render(
        request,
        'app/admins/login.html'
    )

   
def store(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
  

def admin_logout(request):
    logout(request)
    return redirect('/')