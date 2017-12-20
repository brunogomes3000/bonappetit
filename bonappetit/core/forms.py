from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

        class Meta:
                model = Cliente
                fields = ['nome','email','cep','numero','senha']

#class ProdutoCliente(forms.ModelForm):
	#list_dislay