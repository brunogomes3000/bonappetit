# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from .models import Produto
 
class ProdutoAdmin(admin.ModelAdmin):
	list_display = ['nome', 'descricao', 'preco']
	search_fields = ['nome']
	list_filter = ['id_tipoProduto']

admin.site.register(Produto, ProdutoAdmin)

from .models import Tipo_produto
admin.site.register(Tipo_produto)

from .models import Pedido_produto
admin.site.register(Pedido_produto)

from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
	list_filter = ['data', 'forma_pagamento']

admin.site.register(Pedido, PedidoAdmin)


from .models import Cliente
admin.site.register(Cliente)

from .models import Contato
admin.site.register(Contato)
