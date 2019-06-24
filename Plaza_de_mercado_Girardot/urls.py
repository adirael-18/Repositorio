"""Plaza_de_mercado_Girardot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from Plaza.views import Ver_Producto, Insertar_Producto, Editar_Producto, Eliminar_Producto, Ver_Provedor, \
    Insertar_Provedor, Editar_Provedor, Eliminar_Provedor, Ver_Perfil, Insertar_Perfil
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ver_producto/', Ver_Producto.as_view()),
    path('ver_provedor/',Ver_Provedor.as_view()),
    path('ver_perfil/',Ver_Perfil.as_view()),
    path('insertar_provedor/', Insertar_Provedor.as_view()),
    path('insertar_producto/', Insertar_Producto.as_view()),
    path('insertar_perfil/', Insertar_Perfil.as_view()),
    path('editar_producto/<int:pk>/', Editar_Producto.as_view()),
    path('editar_provedor/<int:pk>/', Editar_Provedor.as_view()),
    path('eliminar_provedor/<int:pk>/', Eliminar_Provedor.as_view()),
    path('eliminar_producto/<int:pk>/', Eliminar_Producto.as_view()),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
