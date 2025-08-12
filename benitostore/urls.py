"""
URL configuration for benitostore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from productos.views import ProductoViewSet, CategoriaViewSet
from inventario.views import InventarioViewSet, MovimientoInventarioViewSet

# Unificar todos los viewsets en un solo router
router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'inventario', InventarioViewSet, basename='inventario')
router.register(r'movimiento-inventario', MovimientoInventarioViewSet, basename='movimiento-inventario')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
