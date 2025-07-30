from django.db import models

# Create your models here.
class categoriaclientes(models.Model):
    pass

class clientescredito(models.Model):   
    razon_social = models.CharField(max_length=100)
    ruc = models.CharField(max_length=12, unique=True)
    tiempo_credito = models.IntegerField(default=30)  # Días de crédito

    categoriaclientes = models.ForeignKey(categoriaclientes, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(default=models.timezone.now)
    creado_por = models.CharField(max_length=100, default='admin') 