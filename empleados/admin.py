from django.contrib import admin

from reportes.models import gerente


class empleadosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo', 'fecha_contratacion')
    search_fields = ('nombre', 'apellido', 'cargo')

# Register your models here.
admin.site.register(gerente)
admin.site.register(empleadosAdmin)
