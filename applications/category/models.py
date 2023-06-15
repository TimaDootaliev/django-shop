from django.db import models
from django.db.models.signals import pre_save
from .signals import store_pre_save


class Category(models.Model):
    slug = models.SlugField(primary_key=True, blank=True)
    title = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


pre_save.connect(store_pre_save, Category)
