from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from app.forms import UserForm

def index(request):
    user = User.objects.all()
    return render(
        request,
        'app/user/index.html',
        {
            'user': user
        }
    )
    

def user_login(request):
    page_title = 'Login'
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
        'app/user/login.html',
        {
            'page_title' : page_title
        }
    )

   
def store(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
  

def user_logout(request):
    logout(request)
    return redirect('/')