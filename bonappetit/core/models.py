
from __future__ import unicode_literals

from django.db import models


class Tipo_produto(models.Model):
	descricao = models.CharField('Descrição', max_length=200)
	def __str__(self):
		return self.descricao

class Produto(models.Model):
	nome = models.CharField('Nome', max_length=50)
	descricao = models.CharField('Descrição do alimento', max_length=200)
	preco = models.CharField('Preço', max_length=10)
	id_tipoProduto = models.ForeignKey(Tipo_produto, on_delete=models.CASCADE)
	def __str__(self):
		return self.nome

	class Meta:
		verbose_name = 'Produto'
		verbose_name_plural = 'Produtos'
		ordering = ['nome']

class Cliente(models.Model):
	nome = models.CharField('Nome', max_length=50)
	logradouro = models.CharField('Logradouro', max_length=35, blank=True)
	numero = models.CharField('Número', max_length=20, blank=True)
	cep = models.CharField('Cep', max_length=8, blank=True)
	email = models.EmailField('Email', max_length=30, blank=True)
	senha = models.CharField('Senha', max_length=15)
	admin = models.BooleanField('Administrador')
	def __str__(self):
		return self.nome


class Pedido(models.Model):
	data = models.DateField('Data', auto_now=True, auto_now_add=False)
	forma_pagamento = models.CharField('Forma de Pagamento', max_length=14)
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Pedido_produto(models.Model):
	quantidade = models.CharField('Quantidade', max_length=3)
	id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
	id_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)


class Contato(models.Model):
	numero = models.CharField('Numero', max_length=12)
	id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	def __str__(self):
		return self.id_cliente


class GerenciarAlimento(models.Model):
	codAlimento = models.CharField('CodAlimento ', max_length=50)
	descricao= models.CharField('Descricao', max_length=100)
	porcao = models.CharField('Porcao ', max_length=50)
	preco = models.DecimalField('Preco ', max_digits=5, decimal_places=2)


'''
class Consulta(models.Model):
	nome = models.CharField('Nome', max_length=200)
	produtos = models.ManyToManyField('Produtos',blank=True,null=True)

Consulta.objects.filter(produtos__isnull=False).distinct("id").order_by("id")

consultas = Consulta.objects.annotate(
	mostrar_produtos=models.Count('id_produto')
).filter(
	models.Q(mostrar_produtos__gt=0)
).order_by("-id")
'''