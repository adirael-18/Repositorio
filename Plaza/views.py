from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from Plaza.forms import Formularioprovedor
from .models import Producto,Provedor,Profile
from .forms import Formularioproducto,Formularioperfil

class Ver_Producto(PermissionRequiredMixin, ListView):
    permission_required = 'Plaza.view_producto'
    login_url = 'login'
    model = Producto
    template_name = 'ver_producto.html'
    def get_queryset(self):
        queryset = super(Ver_Producto, self).get_queryset()
        return queryset



class Insertar_Producto(PermissionRequiredMixin, FormView):
    permission_required = 'Plaza.add_producto'
    login_url = 'login'
    form_class = Formularioproducto
    template_name = 'insertar_producto.html'
    success_url = '/ver_producto'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Editar_Producto(PermissionRequiredMixin, UpdateView):
    permission_required = 'Plaza.change_producto'
    login_url = 'login'
    model = Producto
    form_class = Formularioproducto
    template_name = 'editar_producto.html'
    success_url = '/ver_producto'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Eliminar_Producto(PermissionRequiredMixin, DeleteView):
    permission_required = 'Plaza.delete_producto'
    login_url = 'login'
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = '/ver_producto'

class Ver_Provedor(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Provedor
    template_name = 'ver_provedor.html'


class Insertar_Provedor(LoginRequiredMixin, FormView):
    login_url = 'login'
    form_class = Formularioprovedor
    template_name = 'insertar_provedor.html'
    success_url = '/ver_provedor'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Editar_Provedor(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Producto
    form_class = Formularioprovedor
    template_name = 'editar_provedor.html'
    success_url = '/ver_provedor'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Eliminar_Provedor(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Producto
    template_name = 'eliminar_provedor.html'
    success_url = '/ver_provedor'

class Ver_Perfil(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'ver_perfil.html'

class Insertar_Perfil(LoginRequiredMixin, FormView):
    form_class = Formularioperfil
    template_name = 'insertar_perfil.html'
    success_url = '/ver_perfil'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

