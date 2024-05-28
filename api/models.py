from django.db import models

class Cliente (models.Model):
    idCliente = models.PositiveIntegerField (primary_key=True ,max_length=5)
    NombreCliente = models.CharField(max_length=100)
    RutCliente = models.CharField(max_length=100)
    Gmail = models.CharField(max_length=100)
    Contrasenna = models.CharField(max_length=20)

class TipoProducto (models.Model):
    idTipo = models.CharField (primary_key=True ,max_length=4)
    NombreTipo= models.CharField(max_length=100)

    def __str__(self):
        return self.NombreTipo

class Producto (models.Model):
    idProducto = models.PositiveIntegerField (primary_key=True ,max_length=5)
    Tipo_roducto = models.ForeignKey(TipoProducto, related_name='productos', on_delete=models.CASCADE)
    NombreProducto = models.CharField(max_length=100)
    Precio = models.PositiveIntegerField()
    Descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.NombreProducto

# Create your models here.
