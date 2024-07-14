from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        # Create test instances of Menu model
        Menu.objects.create(title="Pizza", price=12.99, inventory=100)
        Menu.objects.create(title="Burger", price=8.99, inventory=50)
    
    def test_getall(self):
        # Initialize the API client
        client = APIClient()
        # Make a GET request to the target view
        response = client.get(reverse('menu-items'))
        # Expected data
        expected_data = [
            {
                "id": 2,
                "title": "Pizza",
                "price": "12.99",
                "inventory": 100
            },
            {
                "id": 3,
                "title": "Burger",
                "price": "8.99",
                "inventory": 50
            }
        ]
        # Assert that the response data matches the expected data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)