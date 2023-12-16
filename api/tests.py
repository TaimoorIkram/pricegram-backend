from django.test import Client
from django.test import TestCase

class APITest(TestCase):
    """
    TESTING STRATEGY:

    - test out all endpoints of the product api
      > 
      > all/
      > products/
        - by brand
        - by cateogry
        - by vendor
      > product/<id>/
      > search/
        - by brand name
        - by category name
        - by vendor name
      > searches/
      > view/
      > visit/ (POST)
      > favourite/
      > unitfavourite/<id>/
      > rmvfavourite/<id>/
      > like/
      > unitlike/<id>/
      > unlike/<id>/
      > review/
      > feedback/
      > feedbacks/
      > matchuser/
    """

    def test_get_all_products(self):
        client = Client()
        result = client.get('/api/products/')
        self.assertEqual(200, result.status_code)
    
    def test_get_specific_product(self):
        client = Client()
        result = client.get('/api/product/1/')
        self.assertEqual(200, result.status_code)
    
    def test_get_specific_product_search_by_brand(self):
        client = Client()
        result = client.get('/api/products/?brand=Dell')
        self.assertEqual(200, result.status_code)
    
    def test_get_specific_product_search_by_category(self):
        client = Client()
        result = client.get('/api/products/?category=Mobile Phones')
        self.assertEqual(200, result.status_code)
    
    def test_get_specific_product_search_by_vendor(self):
        client = Client()
        result = client.get('/api/products/?vendor=Priceoye')
        self.assertEqual(200, result.status_code)
    
    def test_get_search_results(self):
        client = Client()
        expected_result = "Apple iPhone 14 Pro 256GB Storage Physical Sim Non PTA Purple "
        result = client.get('/api/search/?q=Iphone 13')
        self.assertEqual(expected_result, result.json()['products'][0]['title'])
    
    def test_get_search_history_first_one_is_laptop(self):
        client = Client()
        expected_result = "laptops"
        result = client.get('/api/searches/')
        self.assertEqual(expected_result, result.json()[0]['search_query'])