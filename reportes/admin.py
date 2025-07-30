from django.contrib import admin

from reportes.models import reportesadmin

class reportesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
exclude = ('fecha_creacion',)
# Register your models here.
admin.site.register(reportesadmin)