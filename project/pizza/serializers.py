from rest_framework import serializers
from .models import Pizza, Size, Ingredient, InstancePizza, Order


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ('name', 'price')


class PizzaSerializer(serializers.ModelSerializer):
    size = SizeSerializer()
    ingredient = IngredientSerializer(many=True)

    class Meta:
        model = Pizza
        fields = ('id','name', 'size', 'price', 'description', 'slug', 'ingredient',)


class InstancePizzaSerializer(serializers.ModelSerializer):
    size = SizeSerializer()

    class Meta:
        model = InstancePizza
        fields = ("name", "count", "price", "size")


class CartSerializer(serializers.ModelSerializer):
    pizzas = InstancePizzaSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"


class InstanceCartSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()
