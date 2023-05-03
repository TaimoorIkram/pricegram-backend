from django.db import models

NULL = "NULL"

class Product(models.Model):
    title = models.CharField(max_length=1000)
    original_price = models.IntegerField()
    discounted_price = models.IntegerField(blank=True, null=True)
    discount = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    delivery_details = models.CharField(max_length=255, blank=True, null=True)
    delivery_time = models.CharField(max_length=255, blank=True, null=True)
    delivery_fee = models.CharField(max_length=255, blank=True, null=True)
    imgs = models.CharField(max_length=255, blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    avg_score = models.IntegerField(blank=True, null=True)
    max_score = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=3000, blank=True, null=True)
    specifications = models.JSONField(blank=True, null=True)
    review_count = models.IntegerField()
    reviews = models.CharField(max_length=3000, blank=True, null=True)
    recommended_products = models.CharField(max_length=255, blank=True, null=True)
    recommended_products_imgs = models.CharField(max_length=2000, blank=True, null=True)
    
    class Meta:
        db_table = 'restbase_product'
        managed = False