from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Producto, Pedido
from .serializers import ClienteSerializer, ProductoSerializer, PedidoSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        print("FILES:", request.FILES)
        print("DATA:", request.data)

        return super().create(request, *args, **kwargs)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Create your views here.
