from django.contrib import admin

from clientes.models import categoriaclientes, clientescredito

# Register your models here.
admin.site.register(categoriaclientes)
admin.site.register(clientescredito)