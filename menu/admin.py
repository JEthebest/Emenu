from django.contrib import admin

from menu.models import (
    Topping,
    FoodCategory,
    Food,
)


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    pass


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
