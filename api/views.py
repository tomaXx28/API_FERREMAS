from rest_framework import viewsets
from .serializer import ClienteSerializer, ProductoSerializer, TipoProductoSerializer
from .models import Cliente,Producto,TipoProducto


class ClienteViewset(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer


class ProductoViewset(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer


class TipoProductoViewset(viewsets.ModelViewSet):
    queryset=TipoProducto.objects.all()
    serializer_class=TipoProductoSerializer



