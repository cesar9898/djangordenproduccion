from django.db import models

# Create your models here.
class material(models.Model):
    pass

class producto (models.Model):   
    nombreproveedor = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tamaño = models.IntegerField()

    material = models.ForeignKey(material, on_delete=models.PROTECT)
    creado_en = models.DateTimeField(default=models.timezone.now)
    creado_por = models.CharField(max_length=100, default='admin')  