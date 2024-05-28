from rest_framework.response import Response
from rest_framework import viewsets
from .serializer import ClienteSerializer, ProductoSerializer, TipoProductoSerializer
from .models import Cliente,Producto,TipoProducto
from rest_framework import status
from rest_framework.views import APIView


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



