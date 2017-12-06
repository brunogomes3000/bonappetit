# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Produto

from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
	return HttpResponse('Gerenciando ALimentos')

def Produto(request):
	produtos = Produto.object.all(0)
	return render(request, 'index.html')

#terminar a listagem de produtos


