from django.contrib import admin

from inventario.models import material, producto
class productoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    search_fields = ('nombre', 'categoria__nombre')
    
# Register your models here.
admin.site.register(producto)
admin.site.register(material)