from django.test import TestCase
from .models import Product
from applications.category.models import Category
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework.reverse import reverse


User = get_user_model()


factory = APIClient()


class TestProduct(TestCase):
    def setUp(self) -> None:
        user = User.objects.create(
            username="testuser",
            password="superpass123",
            email="test@email.com"
        )
        category = Category.objects.create(title="test category")

        prod = Product.objects.create(
            user=user,
            slug="test-slug",
            title="test title",
            price="2000.00",
            category=category,
            quantity=3,
        )

        self.url = reverse("products-detail", [prod.pk])

    def test_product_is_created(self):
        response = factory.get(self.url)
        self.assertIn('slug', response.json())
        self.assertEqual(response.json()['title'], 'test title')
