from rest_framework import viewsets, generics, filters
from .serializers import PizzaSerializer, CartSerializer
from .models import Pizza, Order
from django_filters.rest_framework import DjangoFilterBackend


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class CartViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = CartSerializer


class PizzaFilterView(viewsets.ModelViewSet):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        queryset = Pizza.objects.all()
        name = self.request.query_params.get('name')
        queryset = queryset.filter(name__istartswith=name)
        return queryset

