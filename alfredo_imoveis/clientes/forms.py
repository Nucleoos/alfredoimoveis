from django import forms
from models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['endereco', 'endereco_cobranca']
        read_only = ['data_cadastro']