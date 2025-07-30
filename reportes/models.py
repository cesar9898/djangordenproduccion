from django.db import models

# Create your models here.
class reportesadmin(models.Model):
    pass

class gerente (models.Model):   
    usuario = models.CharField(max_length=100, empleado=True)
    contrasena = models.CharField(max_length=100)
    
    busqueda_estado_orden = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada')
    ])
    tiempos_entrega = models.IntegerField(default=30)  # Días de entrega