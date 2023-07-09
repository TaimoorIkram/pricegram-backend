from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    slug = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    currency = models.TextField(blank=True, null=True)
    original_price = models.TextField(blank=True, null=True)
    discounted_price = models.TextField(blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    warranty_duration = models.TextField(blank=True, null=True)
    warranty_period = models.TextField(blank=True, null=True)
    warranty_type = models.TextField(blank=True, null=True)
    average_rating = models.TextField(blank=True, null=True)
    num_ratings = models.TextField(blank=True, null=True)
    reviews = models.JSONField(blank=True, null=True)
    specifications = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    similar_products = models.TextField(blank=True, null=True)
    used = models.IntegerField(blank=True, null=True)
    delivery_time_from = models.TextField(blank=True, null=True)
    delivery_time_to = models.TextField(blank=True, null=True)
    delivery_time_period = models.TextField(blank=True, null=True)
    delivery_time_unparsed = models.TextField(blank=True, null=True)
    delivery_fee = models.TextField(blank=True, null=True)
    delivery_details = models.TextField(blank=True, null=True)
    imgs = models.JSONField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    last_updated = models.TextField(blank=True, null=True)

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
    
class Like(models.Model):
    username = models.TextField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    search_time = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.search_time)
    
class Review(models.Model):
    username = models.TextField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  related_name='reviewss')
    average_rating = models.TextField(blank=True, null=True)
    title = models.TextField(max_length=100, null=True)
    stars = models.IntegerField(default=1)
    comment = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)

class BugStatus(models.Model):
    """
    Status of the feedback, if it is a bug report.
    """

    status = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return str(self.status)
       
class SiteFeedback(models.Model):
    """
    User's feedback on issues and improvements in the site features.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=False)
    status = models.ForeignKey(BugStatus, on_delete=models.DO_NOTHING, default=1, related_name='issue_state')
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title + ' - ' + self.status.status)