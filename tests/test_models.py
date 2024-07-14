from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Pizza', price=12.99, inventory=100)
        self.assertEqual(item.title, 'Pizza')