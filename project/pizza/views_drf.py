from rest_framework import viewsets
from .serializers import PizzaSerializer, CartSerializer
from .models import Pizza, Order


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = CartSerializer
