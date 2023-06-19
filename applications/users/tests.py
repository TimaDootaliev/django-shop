from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from utils.utils import get_tokens_for_user

User = get_user_model()


class JWTAuthenticationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'regular user'
        self.password = 'regularpass'
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

        self.admin = User.objects.create_superuser(
            username='admin', password='adminpassword'
        )


    def test_token_generation(self):
        response = self.client.post(
            "/auth/jwt/create/", {"username": self.username, "password": self.password}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_protected_view_access(self):
        token = get_tokens_for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(token.access))
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
