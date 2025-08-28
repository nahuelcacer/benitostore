from rest_framework import serializers
from .models import Producto, Categoria



class CategoriaSerializer(serializers.ModelSerializer):
    subcategorias = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion', 'categoria_padre', 'subcategorias']

    def get_subcategorias(self, obj):
        children = Categoria.objects.filter(categoria_padre=obj.id)
        return CategoriaSerializer(children, many=True).data


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    
    class Meta:
        model = Producto
        fields = [
            'id', 
            'nombre', 
            'descripcion', 
            'precio', 
            'categoria', 
            'categoria_nombre',
            'costo', 
            'margen', 
            'activo', 
            'fecha_creado', 
            'fecha_modificado'
        ]
        read_only_fields = ('fecha_creado', 'fecha_modificado')

    def create(self, validated_data):
        return Producto.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.categoria = validated_data.get('categoria', instance.categoria)
        instance.costo = validated_data.get('costo', instance.costo)
        instance.margen = validated_data.get('margen', instance.margen)
        instance.activo = validated_data.get('activo', instance.activo)
        instance.save()
        return instance