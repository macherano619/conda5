from django.db import models
from django.utils import timezone
from cliente.models import Cliente
# Create your models here.
from django.db import models

class Refugio(models.Model):
    nombre = models.CharField(max_length=144, blank=False, null=False)
    direccion = models.CharField(max_length=144, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    ciudad=models.CharField(max_length=144, blank=False, null=False)

class Perro(models.Model):
    nombre = models.CharField(max_length=144, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    ficha_perro = models.FileField(upload_to="uploads/", blank=True)
    fecha_nacimiento = models.DateTimeField(blank=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.nombre}'
    

    from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    cedula = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
from django.db import models



class DetalleCliente(models.Model):
    id_detalle_cliente = models.AutoField(primary_key=True)
    fecha = models.DateField()
    fecha_f = models.DateField()
    estado = models.CharField(max_length=50)
    comentario = models.TextField()
    programa = models.CharField(max_length=50)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_detalle_cliente)