from rest_framework import serializers

from .models import Category


class CategoryListSerializer(serializers.ListSerializer):
    pass


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["slug", "title"]
        read_only_fields = ["slug"]
