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
    
    def test_get_search_history_first_one_is_laptops(self):
        client = Client()
        expected_result = "laptops"
        result = client.get('/api/searches/')
        self.assertEqual(expected_result, result.json()[0]['search_query'])
    
    def test_add_feedback(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/feedback/', {
            "title": "Good site",
            "comment": "It is missing some things but they will cover up with time"
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual("OK", result.data)
    
    def test_empty_path(self):
        client = Client()
        expected_result = {
            "all/": "Gives all the products",
            "product/<int:id>/": "Gives the product by id",
            "products/": "Gives the products based on filters",
            "search/": "Gives the products based on search results",
            "searches/": "records search history of a user",
            "view/": "records when a user views a product",
            "visit/": "records when a user visits the external link of the product",
            "favourite/": "records the favourite products of a user",
            "like/": "records the likes of the user"
        }
        result = client.get('/api/')
        self.assertEqual(expected_result, result.json())
    
    def test_add_review(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/review/', {
            "id": 1,
            "rating": "It is on average a good item.",
            "title": "Good Item",
            "stars": 5,
            "comment": "This item is very good. I have used it for 2 weeks and I must say, I am impressed."
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
        
    def test_add_like(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/like/', {
            "id": 1,
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
        
    def test_add_favourite(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/favourite/', {
            "id": 1,
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
        
    def test_match_user(self):
        client = Client()
        result = client.get('http://127.0.0.1:8000/api/matchuser/pg', headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result)
        
    def test_unitlike(self):
        client = Client()
        result = client.get('http://127.0.0.1:8000/api/unitlike/1', headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(1, result.product_id)
        
    def test_unitfavourite(self):
        client = Client()
        result = client.get('http://127.0.0.1:8000/api/unitfavourite/1', headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(1, result.product_id)
        
    
    def test_add_visit_external_site(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/visit/', {
            "product_id": 1,
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
        
    def test_add_feedback(self):
        client = Client()
        result = client.post('http://127.0.0.1:8000/api/feedback/', {
            "user": {"username": "pg"},
            "title": "Good Product",
            "comment" : "Quality is good!",
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
        