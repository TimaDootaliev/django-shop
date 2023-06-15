from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save

from .signals import store_pre_save


User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name="Slug ID", primary_key=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    main_image = models.ImageField(upload_to="product-images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        default_related_name = "products"


class ProductImage(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="product-images")

    def __str__(self):
        return str(self.pk)


pre_save.connect(store_pre_save, Product)
