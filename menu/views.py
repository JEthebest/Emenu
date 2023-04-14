from rest_framework import generics

from menu.models import (
    FoodCategory,
)
from menu.serializers import (
    FoodCategorySerializer,
)


class FoodListAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(foods__is_publish=True)
    serializer_class = FoodCategorySerializer


class VeganFoodListAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(foods__is_vegan=True)
    serializer_class = FoodCategorySerializer


class SpecialFoodListAPIView(generics.ListAPIView):
    queryset = FoodCategory.objects.filter(foods__is_special=True)
    serializer_class = FoodCategorySerializer
