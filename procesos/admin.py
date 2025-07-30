from django.contrib import admin

from procesos.models import ordenfacturada

class tiposordenesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

# Register your models here.
admin.site.register(ordenfacturada)
