from django.http import JsonResponse
from django.views import View
from .models import Pizza


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
