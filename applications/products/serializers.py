from rest_framework import serializers
from .models import Product, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        # fmt: off
        fields = [
            "user", "slug", "title",
            "description", "main_image",
            "price", "created_at", "updated_at",
            'images',
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'slug': {'read_only': True},
        }

    def create(self, validated_data: dict):
        validated_data['user'] = self.context['request'].user
        imgs = validated_data.pop('images', None)
        product = Product.objects.create(**validated_data)
        if imgs is not None:
            images = []
            for image in imgs:
                images.append(ProductImage(product_id=product, image=image))
            ProductImage.objects.bulk_create(images)
        return product
    

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(), many=True).data
        return representation
