from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombreCat = models.CharField(max_length=50)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    costo = models.IntegerField(max_length=10)
    existencia = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria,null=True,blank = True, on_delete = models.CASCADE)
    
class Venta(models.Model):
    nombreProducto = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=150)
    costo = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
