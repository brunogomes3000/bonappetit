"""bonappetit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    """
from django.conf.urls import url
from django.contrib import admin
from core.views import Pedido
from core.views import Produto
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

urlpatterns = [
	url(r'^$', views.index, name="index"),
    url(r'^produto/$', views.produto, name="Produto"),
    url(r'^pedido/$', views.pedido, name="Pedido"),
    url(r'^relatorio/$', views.relatorio, name="relatorio"),
	url(r'^usuario/$', views.usuario,name="usuario"),
	url(r'^login/$', login, {'template_name':'login.html'}, name="login"),
	url(r'^produtos/$', views.produtos, name="produtos"),
	url(r'^cadastro/$', views.cadastro, name="cadastro"),
    url(r'^sucesso/$', views.sucesso, name="sucesso"),
    url(r'^consultarAlimentos/$', views.consultarAlimentos, name="consultarAlimentos"),
    url(r'^admin/', admin.site.urls),
    url(r'^usuario/$', views.usuario, name="usuario"),
]



