from django import forms
from .models import Producto, Provedor, Compra, Detallecompra,Venta,Detalleventa, Profile


class Formularioproducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class Formularioperfil(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class Formularioprovedor(forms.ModelForm):
    class Meta:
        model = Provedor
        fields = '__all__'