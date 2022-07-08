from django.db import models
from django.forms import CharField


class User(models.Model):
    name = CharField(max_length=64)


class Restaurant(models.Model):
    name = CharField(max_length=64)


class FoodItem(models.Model):
    name = models.CharField(max_length=64)

class Order(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="orders")
    food_items = models.ManyToManyField(FoodItem, through="OrderFoodItem", related_name="orders")


class OrderFoodItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="order_food_items")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="order_food_items")
    


    



