from django.shortcuts import render
from rest_framework import viewsets
from .models import Item, Pedido
from .serializers import ItemSerializer, PedidoSerializer

# Create your views here.

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer