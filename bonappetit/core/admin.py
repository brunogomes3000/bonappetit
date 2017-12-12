# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Produto
 
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ['nome', 'descricao', 'preco']

admin.site.register(Produto, ProdutoAdmin)

from .models import Tipo_produto
admin.site.register(Tipo_produto)

from .models import Pedido_produto
admin.site.register(Pedido_produto)

from .models import Pedido
admin.site.register(Pedido)

from .models import Cliente
admin.site.register(Cliente)

from .models import Contato
admin.site.register(Contato)
