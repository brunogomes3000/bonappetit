# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Produto
from .models import Pedido_produto
from .models import Pedido
from django.shortcuts import render
from django.http import HttpResponse 


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

def Produto(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos.html')


#terminar a listagem de produtos
def Pedido(request):
	pedido = Pedido.objects.all()


# página de login
def usuario(request):
	return render(request, 'usuario.html')
