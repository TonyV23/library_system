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
from app.views import home,categories

from app import views

urlpatterns = [

    path('', views.home.index, name='home'),
    path('categories/', views.categories.index, name='categories_index'),
    path('categories/create', views.categories.add, name='categories_add'),
    path('categories/store', views.categories.store, name='categories_store'),
    path('categories/edit/<int:id>', views.categories.edit, name='categories_edit'),
    path('categories/delete/<int:id>', views.categories.delete, name='categories_delete'),
]
