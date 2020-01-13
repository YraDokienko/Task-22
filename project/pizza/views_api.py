from django.http import JsonResponse
from django.views import View
from .models import Pizza, Order


class ApiPizzaView(View):

    def get(self, request):
        sort = request.GET.get('sort')
        pizzas = Pizza.objects.all()
        data = []
        if sort:
            pizzas = pizzas.order_by(sort)
        for pizza in pizzas:
            data.append(pizza.get_serialized_pizza())
        return JsonResponse({"pizza_list": data})


class ApiFilterPriceView(View):

    def get(self, request):
        min_price = request.GET.get('min')
        max_price = request.GET.get('max')

        if not min_price:
            min_price = 0

        if not max_price:
            max_price = 999

        data = []
        pizzas = Pizza.objects.filter(price__gt=min_price, price__lt=max_price).order_by('price')
        for pizza in pizzas:
            data.append(pizza.get_serialized_pizza())
        return JsonResponse({"pizza_list": data})


class ApiOrderView(View):

    def get(self, request):
        order = Order.objects.first()
        order_pizza = []
        for pizza in order.pizzas.all():
            order_pizza.append({
                "name": pizza.name,
                "count": pizza.count,
                "price": pizza.price,
            })
        return JsonResponse({"order": order_pizza, "full_price": order.full_price})
