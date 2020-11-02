from django.shortcuts import render, redirect
from myapp.models import *
from myapp.forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def list_carros(request):
    carros = Carro.objects.all()
    cores = Cor.objects.all()
    return render(request, "listas.html", {'carros': carros, 'cores':cores})

def list_jogadores(request):
    jogadores = Jogador.objects.all()
    time = Time.objects.all()
    return render(request, "listas.html", {'jogadores': jogadores, 'time': time})

def list_medicos(request):
    hospitais = Hospitais.objects.all()
    medicos = Medico.objects.all()
    return render(request, "listas.html", {'medicos': medicos, 'hospitais':hospitais})

def list_livros(request):
    livros = Livro.objects.all()
    editoras = Editora.objects.all()
    return render(request, "listas.html", {'livros': livros, 'editoras':editoras})

def add_carro(request):
    if request.method == "POST":
        carro = AddCarro(request.POST)
        if carro.is_valid():
            model_instance = carro.save(commit=False)
            model_instance.save()
            return redirect ('list_carros')
    else:
        carro = AddCarro()
        return render(request, "add_carro.html", {'carro':carro})


def add_time(request):
    if request.method == "POST":
        time = AddTime(request.POST)
        if time.is_valid():
            model_instance = time.save(commit=False)
            model_instance.save()
            return redirect ('list_jogadores')
    else:
        time = AddTime()
        return render(request, "add_time.html", {'time':time})

def add_med(request):
    if request.method == "POST":
        medico = AddMed(request.POST)
        if medico.is_valid():
            model_instance = medico.save(commit=False)
            model_instance.save()
            return redirect ('list_medicos')
    else:
        medico = AddMed()
        return render(request, "add_med.html", {'medico':medico})


def add_livro(request):
    if request.method == "POST":
        livro = AddLivro(request.POST)
        if livro.is_valid():
            model_instance = livro.save(commit=False)
            model_instance.save()
            return redirect ('list_livros')
    else:
        livro = AddLivro()
        return render(request, "add_livro.html", {'livro':livro})
