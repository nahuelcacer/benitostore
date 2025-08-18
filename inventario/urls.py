from rest_framework import routers
from django.urls import path, include
from .views import InventarioViewSet, MovimientoInventarioViewSet
router = routers.DefaultRouter()
router.register(r'inventario', InventarioViewSet)
router.register(r'inventario-movimiento', MovimientoInventarioViewSet)

urlpatterns = router.urls
