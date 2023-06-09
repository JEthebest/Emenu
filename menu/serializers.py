from rest_framework import serializers

from menu.models import (
    Topping,
    FoodCategory,
    Food,
)


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = [
            'name'
        ]


class FoodSerializer(serializers.ModelSerializer):
    toppings = serializers.StringRelatedField(many=True)

    class Meta:
        model = Food
        fields = [
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings'
        ]


class FoodCategorySerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True)

    class Meta:
        model = FoodCategory
        fields = [
            'id',
            'name',
            'foods'
        ]
