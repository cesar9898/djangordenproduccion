from django.db import models

class Tipousuario(models.Model):
    # Add fields for Tipousuario if needed
    pass

class Gerente(models.Model):
    contrasena = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100, unique=True)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    tipo_usuario = models.ForeignKey(Tipousuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
      