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
from app.views import home, authors, borrowers, categories, book, borrows,user


urlpatterns = [
    path ('home/', home.index, name ='home'),

    path('authors/',authors.index,name='authors_index'),
    path('authors/add',authors.add,name='authors_add'),
    path('authors/store',authors.store,name='authors_store'),
    path('authors/edit/<int:id>',authors.edit,name='authors_edit'),
    path('authors/update/<int:id>', authors.update, name="authors_update"),
    path('authors/delete/<int:id>',authors.delete,name='authors_delete'),
    path('authors/details/<int:id>',authors.details,name='authors_details'),
    
    path('categories/', categories.index, name='categories_index'),
    path('categories/add', categories.add, name='categories_add'),
    path('categories/store', categories.store, name='categories_store'),
    path('categories/edit/<int:id>', categories.edit, name='categories_edit'),
    path('categories/update/<int:id>', categories.update, name="categories_update"),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),

    path('books/', book.index, name='books_index'),
    path('books/add', book.add, name='books_add'),
    path('books/store', book.store, name='books_store'),
    path('books/edit/<int:id>', book.edit, name='books_edit'),
    path('books/update/<int:id>', book.update, name="books_update"),
    path('books/delete/<int:id>', book.delete, name='books_delete'),

    path('borrowers/', borrowers.index, name="borrowers_index"),
    path('borrowers/add', borrowers.add, name='borrowers_add'),
    path('borrowers/store',borrowers.store,name='borrowers_store'),
    path('borrowers/edit/<int:id>', borrowers.edit, name='borrowers_edit'),
    path('borrowers/update/<int:id>', borrowers.update, name="borrowers_update"),
    path('borrowers/delete/<int:id>', borrowers.delete, name='borrowers_delete'),
    
    path('borrows/',borrows.index , name='borrows_index'),
    path('borrows/add',borrows.add, name='borrows_add'),
    path('borrows/store',borrows.store, name='borrows_store'),
    path('borrows/edit/<int:id>',borrows.edit, name='borrows_edit'),
    path('borrows/update/<int:id>', borrows.update, name="borrows_update"),
    path('borrows/delete/<int:id>',borrows.delete, name='borrows_delete'),
    path('borrows/getBooks',borrows.getBooks, name='borrows_getBooks'),

    path('user/', user.index, name='user_index'),
    path('', user.admin_login, name='user_login'),
    path('user/store', user.store, name='user_store'),
    path('logout/', user.admin_logout, name='logout'),

]
