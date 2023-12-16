from django.test import Client
from django.test import TestCase

class TestRoutines(TestCase):
    def test_visit_item_and_like(self):
        """
        Visit a product's page and like that product and end the test case.
        """

        client = Client()
        visited_product = client.get('/api/product/1/')
        result = client.post('/api/like/', {
            'product_id': visited_product.json()['product']['id'],
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
    

    def test_visit_item_and_review(self):
        """
        Visit a product's page and review that product and end the test case.
        """

        client = Client()
        visited_product = client.get('/api/product/1/')
        result = client.post('/api/review/', {
            "username": "pg",
            "id": visited_product.json()['product']['id'],
            "rating": "It is on average a good item.",
            "title": "Good Item",
            "stars": 5,
            "comment": "This item is very good. I have used it for 2 weeks and I must say, I am impressed."
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(200, result.status_code)
