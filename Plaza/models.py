from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile (models.Model):
    Genero=((1,"Masculino"),
            (2,"Femenino"),
            (3,"Otro"),)
    documento=models.CharField(max_length=50)
    telefono=models.CharField(max_length=50)
    nacimiento=models.DateField()
    genero=models.SmallIntegerField(choices=Genero)
    user=models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table='profile'


class Provedor (models.Model):
    Rango_social = ((1, "uno"),
                    (2, "dos"),
                    (3, "otro"),)
    rango = models.SmallIntegerField(choices=Rango_social)
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    class Meta:
        db_table = 'proveedor'

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)



class Producto (models.Model):
    Estado = ((1, "Aprobada"),
              (2, "Rechadaza"),
              (3, "Ejecutada"),)
    Stock = ((1, "Abarrotes"),
              (2, "Carnes"),
              (3, "Pescado"),)
    nombre = models.CharField(max_length=45)
    stock = models.SmallIntegerField(choices=Stock)
    valorcosto = models.CharField(max_length=45)
    estado = models.SmallIntegerField(choices=Estado)
    valorventa = models.CharField(max_length=45)
    provedor = models.ForeignKey(Provedor, on_delete=models.PROTECT)

    class Meta:
        db_table = 'producto'

    def __str__(self):
        return self.stock

    def __str__(self):
        return self.estado

class Compra (models.Model):
    fecha = models.DateField()
    total = models.IntegerField()

    class Meta:
        db_table = 'compra'


class Detallecompra (models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    compra = models.ForeignKey(Compra, on_delete=models.PROTECT)

    class Meta:
        db_table = 'detallecompra'


class Venta (models.Model):
    fecha = models.DateField()
    total = models.IntegerField()
    iva =models.CharField(max_length=50)

    class Meta:
        db_table = 'venta'


class Detalleventa (models.Model):
    cantidad = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

    class Meta:
        db_table = 'detalleventa'