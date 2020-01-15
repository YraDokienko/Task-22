from rest_framework import serializers
from .models import Pizza, Size, Ingredient


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
        fields = ('name', 'size', 'price', 'description', 'slug', 'ingredient',)