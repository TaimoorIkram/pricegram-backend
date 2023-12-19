from django.test import Client
from django.test import TestCase

class TestRoutines(TestCase):
    """
    TESTING STRATEGY:

    - test all usage scenarios of the webiste that include:
      > visiting a product and then liking the product
      > visiting a product and leaving a review for that item
      > authenticating a user and viewing the liked products
      > searching for a product, visiting it, liking and viewing the liked products
      > viewing the search history after searching for an item "iphone"
    """

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
    
    def test_search_and_view_history(self):
        """
        Search for a product and then visit the search history to see the most recent search.
        """

        client = Client()
        expected_result = 'iphone'
        searched_query = client.get(f'/api/search/?q={expected_result}')
        result = client.get('/api/searches/', headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(expected_result, result.json()[0]['search_query'])

    def test_search_iphone_visit_first_like_and_view_liked_products(self):
        """
        Searches for 'iphone', visits the first product that appears in the search results and then likes that product and views it in liked products to make sure the like is registered.
        """

        client = Client()
        search_query = 'iphone'
        searched_query = client.get(f'/api/search/?q={search_query}')
        visiting_item = searched_query.json()['products'][0]['id']
        liked_item = client.post(f'/api/like/', {
            'product_id': visiting_item,
        }, headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        result = client.get('/api/like/', headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5MDQ1MDQ1LCJpYXQiOjE3MDI3MzE0NDUsImp0aSI6IjE1MDMzODA0ZWZiZDRkYTViMWU3OWQxNWE1NzE5NzJlIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJwZyJ9.RddHoigg3iRrIo1wLrwS90UQkgL8TNcm6Z0G_1KkpA8"})
        self.assertEqual(visiting_item, result.json()[0]['id'])
