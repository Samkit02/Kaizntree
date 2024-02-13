from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from authentication.models import CustomUser

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('api_token_auth')
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'testusertest',
            'password': 'testpassword',
            'security_question': 'What is your favorite color?',
            'security_answer': 'Blue'
        }

    def test_login(self):
        # Create a test user
        CustomUser.objects.create_user(username='testusertest', password='testpassword')

        # Attempt to log in
        response = self.client.post(self.login_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_register(self):
        # Attempt to register a new user
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)
