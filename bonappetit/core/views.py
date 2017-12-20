# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Produto
from .models import Pedido_produto
from .models import Pedido
from .models import Tipo_produto
from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import ClienteForm

#controlador da PÁGINA produtos
def produtos(request):
	produtos = Produto.objects.all()
	context = {
		'produtos': produtos
	}
	return render(request, 'produtos.html', context)

#controlador da PÁGINA cadastro
def cadastro(request):
	return render(request, 'cadastro.html')	

def usuario(request):
	return render(request, 'usuario.html')

def consultarAlimentos(request):
	id_tipoProduto = Tipo_produto.objects.all()
	#produtos.objects.get(id_tipoProduto=’12345678901’)

	if request.method == 'GET':
		if 'nome' in request.GET:
			nome=request.GET.get("nome")
		else:
			nome=""
		if 'tipoProdutoget' in requst.GET and request.GET.get("tipoProdutoget")!="Escolha um produto":
			tipoProdutoget=request.GET.get('tipoProdutoget')
		else:
			tipoProdutoget=Produto.objects.values_list('id')




	context = {
		'nome': nome,
		'tipoProfutoget': id_tipoProduto,
		'produtos': produtos
	}
	return render(request, 'consultarAlimentos.html', context)
	


def index(request):

	return render(request, 'index.html')


	#return HttpResponse('Gerenciando ALimentos')

def produto(request):
	produtos = Produto.objects.all()
	return render(request, 'produtos.html')



#terminar a listagem de produtos

def cadastro(request):
	form = UserCreationForm(request.POST or None)
	form2 = ClienteForm(request.POST or None)
	context = {
		'form': form,
		'form2': form2
	}
	if request.method == 'POST':
		if form.is_valid():
			user_post = UserCreationForm(request.POST)
			user = user_post.save(commit=False)
			user.set_password(user_post.cleaned_data['password1'])
			user.save()
			return redirect('/sucesso')
	return render(request, 'cadastro.html', context)

	@login_required(login_url='login')
	def usuario(request):
		return render (request, 'usuario.html')



def pedido(request):
	pedido = Pedido.objects.all()


# página de login
def usuario(request):
	return render(request, 'usuario.html')

def relatorio(request):
	return render(request, 'relatorio.html')

def sucesso(request):
	return render(request, 'sucesso.html')

