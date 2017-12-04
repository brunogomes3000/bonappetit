# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Gerenciaralimento(models.Model):
	codAlimento = models.CharField('CodAlimento ', max_length=50)
	descricao= models.CharField('Descricao', max_length=100)
	porcao = models.CharField('Porcao ', max_length=50)
	preco = models.DecimalField('Preco ', max_digits=5, decimal_places=2)

