from rest_framework import serializers

from product.models import (
    Product as ProductModel,
    Price as PriceModel
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceModel
        fields = "__all__"