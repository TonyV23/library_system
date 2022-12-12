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
from app.views import home, categories, authors, book


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', authors.index,name='home'),

    path('authors/',authors.index,name='authors_index'),
    path('authors/add',authors.add,name='authors_add'),
    path('authors/store',authors.store,name='authors_store'),
    path('authors/edit/<int:id>',authors.edit,name='authors_edit'),
    path('authors/delete/<int:id>',authors.delete,name='authors_delete'),

    path('', categories.index, name='home'),
    path('categories/', categories.index, name='categories_index'),
    path('categories/create', categories.add, name='categories_add'),
    path('categories/store', categories.store, name='categories_store'),
    path('categories/edit/<int:id>', categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),


    path('books/', book.index, name='books_index'),
    path('books/add', book.add, name='books_add'),
    path('books/store', book.store, name='books_store'),
    path('books/edit/<int:id>', book.edit, name='books_edit'),
    path('books/delete/<int:id>', book.delete, name='books_delete'),
]
