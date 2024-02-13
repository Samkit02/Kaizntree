from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import CustomUser
from .models import InventoryItem

class DashboardTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.items_url = reverse('item_dashboard')
        self.user = CustomUser.objects.create_user(username='testusertest', password='testpassword')
        self.item = InventoryItem.objects.create(
            sku='SKU001',
            name='Test Item',
            category='Test Category',
            tags='Test Tag',
            stock_status='In Stock',
            available_stock=10,
            owner=self.user
        )

    def test_get_items_authenticated(self):
        # Authenticate the client
        self.client.force_authenticate(user=self.user)

        # Retrieve items
        response = self.client.get(self.items_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
