from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['nombre']
    ordering = ['nombre']

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer   
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['categoria', 'activo']  # Requiere django-filter
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['precio', 'fecha_creado', 'nombre']
    ordering = ['-fecha_creado']
    
    def perform_create(self, serializer):
        producto = serializer.save()
        # Crear inventario asociado al producto
        from inventario.models import Inventario
        Inventario.objects.create(producto=producto, cantidad=0)
    
    @action(detail=False, methods=['get'])
    def activos(self, request):
        """Endpoint personalizado para obtener solo productos activos"""
        productos_activos = Producto.objects.filter(activo=True)
        serializer = self.get_serializer(productos_activos, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        """Endpoint para obtener productos agrupados por categoría"""
        categoria_id = request.query_params.get('categoria_id', None)
        if categoria_id:
            productos = Producto.objects.filter(categoria=categoria_id, activo=True)
            serializer = self.get_serializer(productos, many=True)
            return Response(serializer.data)
        return Response({'error': 'Se requiere categoria_id'}, status=400)