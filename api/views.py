from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ClienteSerializer, ProductoSerializer, TipoProductoSerializer
from .models import Cliente,Producto,TipoProducto
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class ClienteViewset(viewsets.ModelViewSet):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer


class ProductoViewset(viewsets.ModelViewSet):
    queryset=Producto.objects.all()
    serializer_class=ProductoSerializer


class TipoProductoViewset(viewsets.ModelViewSet):
    queryset=TipoProducto.objects.all()
    serializer_class=TipoProductoSerializer



class DetalleCliente(APIView):
    def get(self, request, idCliente, format=None):
        try:
            cliente = Cliente.objects.get(idCliente=idCliente)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)

    def put(self, request, idCliente, format=None):
        try:
            cliente = Cliente.objects.get(idCliente=idCliente)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, idCliente, format=None):
        try:
            cliente = Cliente.objects.get(idCliente=idCliente)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idCliente, format=None):
        try:
            cliente = Cliente.objects.get(idCliente=idCliente)
        except Cliente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getProductos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)


def productos_por_tipo(request):
    tipo_producto = request.GET.get('tipo_producto', None)
    if tipo_producto:
        productos = Producto.objects.filter(Tipo_roducto__NombreTipo=tipo_producto)
    else:
        productos = Producto.objects.all()
    
    productos_list = list(productos.values())
    return JsonResponse(productos_list, safe=False)
