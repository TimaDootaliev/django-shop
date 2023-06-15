from slugify import slugify

from utils.utils import now


def store_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title) + now()
    instance.in_stock = instance.quantity > 0
