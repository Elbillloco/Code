from django.test import TestCase


class HelloWorldTests(TestCase):
    def test_homepage_returns_hello_world(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello world"})
