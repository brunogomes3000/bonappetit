# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Produto
from .models import Pedido_produto
from .models import Pedido



from django.shortcuts import render
from django.http import HttpResponse 

def consultarAlimentos(request):
	return render(request, 'consultarAlimentos.html')
	produtos.objects.all()

def Produto(request):
	produtos = Produto.object.all(0)
	return render(request, 'produtos.html')


#terminar a listagem de produtos


def Pedido(request):
	pedido = Pedido.object.all(0)
