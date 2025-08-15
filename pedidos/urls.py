
from rest_framework import routers
from django.urls import path, include
from .views import PedidoViewSet
router = routers.DefaultRouter()
router.register(r'pedidos', PedidoViewSet)

urlpatterns = router.urls
