from django.shortcuts import render, redirect
from .models import Cliente
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Cliente
from .forms import ClienteForm
from django.core.urlresolvers import reverse_lazy

from django.views.generic.edit import UpdateView

class ClienteUpdate(UpdateView):
    model = Cliente
    fields=('nombre', 'telefono', 'direccion','foto')
    success_url = reverse_lazy('clientes:clientes')
    	

class ListaCliente(ListView):
	model= Cliente


class DetalleCliente(DetailView):
	model = Cliente

def agregar_cliente(request):

	if request.method=='POST':
		form=ClienteForm(request.POST, request.FILES)
		if form.is_valid():
			cliente = form.save()
			cliente.save()
			return HttpResponseRedirect('/')
	else:
		form = ClienteForm()		
		

	template=loader.get_template('agregar.html')
	context={
		'form': form
	}
	return HttpResponse(template.render(context,request))	

def borrar_cliente(request, id):
	cliente = Cliente.objects.get(id=id)
	cliente.delete()
		
	return HttpResponseRedirect('/')		