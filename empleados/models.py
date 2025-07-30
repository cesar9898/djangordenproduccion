class tipousuario (models.Model):

  class gerente  (models.Model):
     contrasena = models.CharField(max_length=100)
     usuario = models.CharField(max_length=100, unique=True)
   
     
   class empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_contratacion = models.DateTimeField(auto_now_add=True)
    tipo_usuario = models.ForeignKey(tipousuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
      