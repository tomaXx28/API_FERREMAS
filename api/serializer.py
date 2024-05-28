from rest_framework import serializers
from .models import Cliente, Producto, TipoProducto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Cliente
        fields= '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model= TipoProducto
        fields= '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Producto
        fields= '__all__'

