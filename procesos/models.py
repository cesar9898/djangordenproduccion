from django.db import models

# Create your models here.
class tiposordenes(models.Model):
    ordenoffset = models.CharField(max_length=100, unique=True)
    ordendigital = models.CharField(max_length=100, unique=True)
    ordenrotulacion = models.CharField(max_length=100, unique=True)
    pass

class ordenfacturada (models.Model):   
    numero_orden = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField()
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada')
    ])
    usuario = models.CharField(max_length=100, empleado=True)
    contrasena = models.CharField(max_length=100)