# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Produto
from .models import Pedido_produto
from .models import Pedido
from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm


#controlador da PÁGINA produtos
def produtos(request):
	return render(request, 'produtos.html')


#controlador da PÁGINA cadastro
def cadastro(request):
	return render(request, 'cadastro.html')	

def consultarAlimentos(request):
	produtos = Produto.objects.all()
	context = {
		'produtos': produtos
	}
	return render(request, 'consultarAlimentos.html', context)
	


def index(request):

	return render(request, 'index.html')


	#return HttpResponse('Gerenciando ALimentos')

def produto(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos.html')



def cadastro(request):
	form = UserCreationForm(request.POST or None)
	form2 = UserCreationForm(request.POST or None)
	context = {
		'form': form,
		'form2': form2
	}
	if request.method == 'POST':
		if form.is_valid():
			user_post = UserCreationForm(request.POST)
			user = user_post.save(commit=False)
			user.set_password(user_post.cleaned_data['password'])
			user.save()
		form.save()
	return render(request, 'cadastro.html', context)


def pedido(request):

	pedido = Pedido.objects.all()


# página de login
def usuario(request):
	return render(request, 'usuario.html')
