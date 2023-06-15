from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}
