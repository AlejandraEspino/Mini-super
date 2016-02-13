from django.conf.urls import url	
from . import views
from .views import ListaCliente,DetalleCliente,agregar_cliente,borrar_cliente

urlpatterns=[
	url(r'^$', views.ListaCliente.as_view(), name='clientes'),
	url(r'^cliente/(?P<pk>[0-9]+)/$', views.DetalleCliente.as_view(), name="detalle"),
	url(r'^cliente/agregar', views.agregar_cliente, name="agregar"),
	url(r'^cliente/(?P<id>\d+)$', views.borrar_cliente, name="borrar"),
	url(r'^cliente/(?P<pk>\d+)/update/$', views.ClienteUpdate.as_view(), name='update'),

]
