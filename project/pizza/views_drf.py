from rest_framework import viewsets
from .serializers import PizzaSerializer, CartSerializer, InstanceCartSerializer
from .models import Pizza, Order, InstancePizza
from django.http import JsonResponse


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


class PizzaToCartView(viewsets.ModelViewSet):
    queryset = InstancePizza.objects.all()
    serializer_class = InstanceCartSerializer

    def create(self, request, *args, **kwargs):
        order = Order.objects.first()
        if not order:
            order = Order.objects.create()

        pizza_id = request.GET.get('id')
        count = request.GET.get('count')
        instance_pizza = InstancePizza.objects.filter(pizza_template=pizza_id)

        if instance_pizza:
            instance_pizza = InstancePizza.objects.get(pizza_template=pizza_id)
            instance_pizza.count += int(count)
            instance_pizza.save()

        else:
            pizza = Pizza.objects.get(id=pizza_id)
            instance_pizza = InstancePizza.objects.create(
                name=pizza.name,
                size=pizza.size,
                price=pizza.price,
                count=count,
                pizza_template=pizza
            )

            order.pizzas.add(instance_pizza)
        order.save_full_price()
        return JsonResponse({"message": "Pizza add to cart!"})


