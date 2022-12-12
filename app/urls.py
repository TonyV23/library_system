"""library_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app.views import home,book

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home.index,name='home'),

    path('books/', book.index, name='books_index'),
    path('books/add', book.add, name='books_add'),
    path('books/store', book.store, name='books_store'),
    path('books/edit/<int:id>', book.edit, name='books_edit'),
    path('books/delete/<int:id>', book.delete, name='books_delete'),
]
