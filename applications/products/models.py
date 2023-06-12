from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify

from .utils import now

User = get_user_model()


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(verbose_name="Slug ID", primary_key=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    main_image = models.ImageField(upload_to="product-images")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


@receiver(pre_save, sender=Product)
def store_pre_save(sender, instance: Product, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title) + now()


class ProductImage(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="product-images")

    def __str__(self):
        return str(self.pk)
