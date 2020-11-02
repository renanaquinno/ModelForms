from django.forms import ModelForm
from myapp.models import  *
from django import forms

class AddCarro(ModelForm):
    class Meta:
        model = Cor
        fields = ['cor', 'carro']

class AddTime(ModelForm):
    class Meta:
        model = Jogador
        fields = ['jogador', 'time']

class AddMed(ModelForm):
    class Meta:
        model = Hospital
        fields = ['nome', 'Medico']

class AddLivro(ModelForm):
    class Meta:
        model = Editora
        fields = ['nome', 'livro']
