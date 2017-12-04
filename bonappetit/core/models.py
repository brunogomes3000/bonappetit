# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Tipo_produto(models.Model):
	descricao = models.CharField('Descrição', max_length=200)

class Produto(models.Model):
	descricao = models.CharField('Descrição', max_length=200)
	nome = models.CharField('Nome', max_length=50)
	preco = models.CharField('Preço', max_length=4)
	id_tipoProduto = models.ForeignKey(Tipo_produto, on_delete=models.CASCADE)
	def __str__(self):
		return self.nome

class Cliente(models.Model):
	email = models.CharField('Email', max_length=20)
	senha = models.CharField('Senha', max_length=15)
	nome = models.CharField('Nome', max_length=50)
	cep = models.CharField('Cep', max_length=8)
	logradouro = models.CharField('Logradouro', max_length=30)
	numero = models.CharField('Numero', max_length=3)
	admin = models.BooleanField('Administrador')
	def __str__(self):
		return self.nome



class Pedido(models.Model):

	data = models.DateField(auto_now=True, auto_now_add=False)
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

class Gerenciaralimento(models.Model):
	codAlimento = models.CharField('CodAlimento ', max_length=50)
	descricao= models.CharField('Descricao', max_length=100)
	porcao = models.CharField('Porcao ', max_length=50)
	preco = models.DecimalField('Preco ', max_digits=5, decimal_places=2)


