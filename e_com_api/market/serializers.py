from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id', 'name', 
            'category', 'price', 
            'get_image', 'get_thumbnail', 
            'description', 'get_absolute_url', 
        )   


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )