from django.db import models

class Product(models.Model):
    slug = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    original_price = models.TextField(db_column='original price', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    discounted_price = models.TextField(db_column='discounted price', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    address = models.TextField(blank=True, null=True)
    delivery_time_from = models.TextField(blank=True, null=True)
    delivery_time_to = models.TextField(blank=True, null=True)
    delivery_time_period = models.TextField(blank=True, null=True)
    delivery_time_unparsed = models.TextField(blank=True, null=True)
    delivery_fee = models.TextField(blank=True, null=True)
    imgs = models.JSONField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    average_rating = models.TextField(blank=True, null=True)
    num_ratings = models.TextField(blank=True, null=True)
    reviews = models.TextField(blank=True, null=True)
    similer_products = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    vendor_url = models.TextField(blank=True, null=True)
    warranty_duration = models.TextField(blank=True, null=True)
    warranty_period = models.TextField(blank=True, null=True)
    last_updated = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    specifications = models.JSONField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    warranty_type = models.TextField(blank=True, null=True)
    delivery_details = models.TextField(blank=True, null=True)
    original_price_0 = models.TextField(db_column='original_price', blank=True, null=True)  # Field renamed because of name conflict.
    discounted_price_0 = models.TextField(db_column='discounted_price', blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'product'

class SearchHistory(models.Model):
    username = models.TextField(blank=True, null=True)
    search_query = models.TextField(blank=True, null=True)
    search_time = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.search_time)
    
class ViewHistory(models.Model):
    username = models.TextField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    search_time = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.search_time)
    
class VisitHistory(models.Model):
    username = models.TextField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    search_time = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.search_time)
    
class Favourite(models.Model):
    username = models.TextField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    search_time = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.search_time)
    
