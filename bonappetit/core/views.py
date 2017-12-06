# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
	return HttpResponse('Gerenciando ALimentos')

def index(request):
	return render(request, 'index.html')

# Create your views here.
<<<<<<< HEAD









=======
def index (request):
	return render(request, 'index.html')
>>>>>>> 0150649f373f9a6866b4e6fba43bd3ff444f4380
