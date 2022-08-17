from re import A
from django.db import models

class Remera(models.Model):
    marca = models.CharField(max_length=50)
    talle = models.CharField(max_length=4)
    precio = models.FloatField()
    stock = models.IntegerField()

    def __str__(self) -> str: 
        return f"(Marca: {self.marca}, talle {self.talle}, $ {self.precio}"

class Pantalon(models.Model):
    marca = models.CharField(max_length=50)
    talle = models.CharField(max_length=4)
    precio = models.FloatField()
    tipo = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self) -> str: 
        return f"(Marca: {self.marca}, talle {self.talle}, $ {self.precio}, tipo {self.tipo})"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    contraseña = models.IntegerField()

    def __str__(self) -> str: 
        return f"(Nombre: {self.nombre} {self.apellido}, mail {self.email})"

