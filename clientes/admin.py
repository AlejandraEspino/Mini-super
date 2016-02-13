from django.contrib import admin
from clientes.models import Cliente

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'direccion','foto')
