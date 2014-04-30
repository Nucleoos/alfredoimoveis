__author__ = 'gpzim98'
from django import forms
from models import Endereco, Bairro

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco

class BairroForm(forms.ModelForm):
    class Meta:
        model = Bairro
        fields = ['nome', 'cidade']
        readonly = ('codigo',)