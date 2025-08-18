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
from pedidos.urls import router as pedidos_router
from productos.urls import router as productos_router
from inventario.urls import router as inventario_router

router = DefaultRouter()
router.registry.extend(pedidos_router.registry)
router.registry.extend(productos_router.registry)
router.registry.extend(inventario_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('userauth.urls'))
]
