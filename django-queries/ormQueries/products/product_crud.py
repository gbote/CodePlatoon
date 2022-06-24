from .models import Product 
from django.db.models import Q, Avg, Max
from django.db.models.functions import Length

class ProductCrud:
    desc = "This is my Product Crud class"

    @staticmethod
    def get_all_products():
        return Product.objects.all() 

    @staticmethod
    def find_by_model(model_name):
        ## SELECT * FROM products WHERE model=model_name
        return Product.objects.get(model=model_name) ## .get() should only return one result, else will be an ERROR!!! 

    @staticmethod
    def last_record():
        return Product.objects.last()

    @staticmethod
    def by_rating(desired_rating):
        return Product.objects.filter(rating=desired_rating) ## .filter() can return more than one result!

    @staticmethod
    def by_rating_range(min_rating, max_rating):
        return Product.objects.filter(rating__range=(min_rating, max_rating))

    @staticmethod
    def by_rating_and_color(desired_rating, desired_color):
        return Product.objects.filter(rating=desired_rating, color=desired_color)

    @staticmethod
    def by_rating_or_color(desired_rating, desired_color):
       return Product.objects.filter(Q(rating=desired_rating) | Q(color=desired_color))
        #return Product.objects.filter(rating=desired_rating) | Product.objects.filter(color=desired_color)

    @staticmethod
    def no_color_count():
        return Product.objects.filter(color=None).count()

    @staticmethod
    def below_price_or_above_rating(below_price, above_rating):
        return Product.objects.filter(price_cents__lt=below_price) | Product.objects.filter(rating__gt=above_rating)

    @staticmethod
    def ordered_by_category_alphabetical_order_and_then_price_decending():
        return Product.objects.all().order_by("category", "-price_cents")

    @staticmethod
    def products_by_manufacturer_with_name_like( namelike):
        return Product.objects.filter(manufacturer__icontains=namelike) 

    @staticmethod
    def manufacturer_names_for_query(manu_name):
        records = Product.objects.filter(manufacturer__icontains=manu_name)
        return [r.manufacturer for r in records]

    @staticmethod
    def not_in_a_category(category):
        return Product.objects.exclude(category=category)

    @staticmethod 
    def limited_not_in_a_category(category, limit):
        return ProductCrud.not_in_a_category(category)[:limit]

    @staticmethod
    def category_manufacturers(desired_category):
        return Product.objects.filter(category=desired_category).values_list("manufacturer", flat=True)

    @staticmethod
    def average_category_rating(category):
        return Product.objects.filter(category=category).aggregate(Avg("rating"))

    @staticmethod
    def greatest_price():
        return Product.objects.aggregate(Max("price_cents"))

    @staticmethod
    def longest_model_name():
        r = Product.objects.order_by(-Length("model")).values_list("id", flat=True)
        return r[0]

    @staticmethod
    def ordered_by_model_length():
        return Product.objects.order_by(Length("model"))