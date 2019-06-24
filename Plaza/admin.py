from django.contrib import admin
from django.contrib import admin
from .models import Provedor,Producto,Compra,Detallecompra,Venta,Detalleventa,Profile

# Register your models here.
@admin.register(Provedor)
class Adminprovedor(admin.ModelAdmin):
    list_display = ('user','rango','nombre_provedor',)
    list_filter =  ('rango',)

    def nombre_provedor(self, prov):
        return '%s %s' % (prov.user.first_name, prov.user.last_name)



@admin.register(Producto)
class Adminproducto(admin.ModelAdmin):
    list_display =  ('nombre','stock','valorcosto','estado','valorventa','provedor',)
    list_filter =  ('estado',)

@admin.register(Compra)
class Admincompra(admin.ModelAdmin):
    list_display = ('fecha','total',)

@admin.register(Detallecompra)
class Admindetallecompra(admin.ModelAdmin):
    list_display = ('cantidad','producto','compra',)

@admin.register(Venta)
class Adminventa(admin.ModelAdmin):
    list_display = ('fecha','total','iva',)

@admin.register(Detalleventa)
class Admindetalleventa(admin.ModelAdmin):
    list_display = ('cantidad','producto','venta',)

@admin.register(Profile)
class Adminprofile(admin.ModelAdmin):
    list_display = ('genero', 'telefono', 'nacimiento', 'genero', 'user',)
    list_filter = ('genero',)
