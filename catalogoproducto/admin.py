from django.contrib import admin

from catalogoproducto.models import categoria
from inventario.models import producto

# Register your models here.
admin.site.register(categoria)
admin.site.register(producto)
