from django.db import models


class Topping(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Название ингредиента',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'


class FoodCategory(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Название категрии блюд',
    )
    is_publish = models.BooleanField(
        default=False,
        verbose_name='Is publish'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Food(models.Model):
    name = models.CharField(
        max_length=60,
        verbose_name='Название блюда',
    )
    description = models.CharField(
        max_length=90,
        verbose_name='Описание'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    category = models.ForeignKey(
        FoodCategory,
        related_name='foods',
        on_delete=models.CASCADE,
        verbose_name='Категория блюда'
    )
    toppings = models.ManyToManyField(
        Topping,
        verbose_name='Ингредиенты'
    )
    is_vegan = models.BooleanField(
        default=False,
        verbose_name='Is vegan'
    )
    is_publish = models.BooleanField(
        default=False,
        verbose_name='Is publish'
    )
    is_special = models.BooleanField(
        default=False,
        verbose_name='Is special'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
