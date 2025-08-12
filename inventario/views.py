from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Inventario, MovimientoInventario
from django.db.models import F
from .serializers import InventarioSerializer, MovimientoInventarioSerializer

# Create your views here.
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['producto__nombre', 'producto__id']
    ordering_fields = ['cantidad']




class MovimientoInventarioViewSet(viewsets.ModelViewSet):
    queryset = MovimientoInventario.objects.all()
    serializer_class = MovimientoInventarioSerializer
    
    filterset_fields = ['inventario', 'tipo_movimiento']
    search_fields = ['inventario__producto__nombre']
    ordering_fields = ['fecha']

    def perform_create(self, serializer):
        instance = serializer.save()
        match instance.tipo_movimiento:
            case 'entrada':
                op = F('cantidad') + instance.cantidad
            case 'salida':
                op = F('cantidad') - instance.cantidad
            case _:
                raise ValueError("Tipo de movimiento no válido")

        Inventario.objects.filter(id=instance.inventario.id).update(cantidad=op)
       