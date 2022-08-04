from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length = 255, blank = False)

    def __str__(self):
        return self.category_name

class Post(models.Model):
    title = models.CharField(max_length = 255, blank = False)
    description = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 5, decimal_places = 2)
    seller = models.CharField(max_length = 255)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, default = 1)

    def __str__(self):
        return self.title
