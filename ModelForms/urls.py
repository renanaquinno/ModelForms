"""ModelForms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_carro', views.add_carro, name = 'add_carro'),
    path('add_time', views.add_time, name = 'add_time'),
    path('add_med', views.add_med, name = 'add_med'),
    path('add_livro', views.add_livro, name = 'add_livro'),
    path('list_carros', views.list_carros, name='list_carros'),
    path('list_jogadores', views.list_jogadores, name='list_jogadores'),
    path('list_medicos', views.list_medicos, name='list_medicos'),
    path('list_livros', views.list_livros, name='list_livros'),
]
