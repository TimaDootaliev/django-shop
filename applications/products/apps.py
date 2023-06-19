from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "applications.products"

    def ready(self) -> None:
        from django.db.models.signals import pre_save
        from .signals import store_pre_save
        from .models import Product

        pre_save.connect(store_pre_save, Product)
