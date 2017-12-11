# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
	return HttpResponse('Gerenciando ALimentos')

def index(request):
	return render(request, 'index.html')

def Pedido(request):
	pedido = Pedido.object.all(0)
	# código que liste as vendas realizadas durante uma data determinada