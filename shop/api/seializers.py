from rest_framework import serializers
from shop.models import Category, Product, ProductPhoto, ProductColor, ProductSize


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']


class ProductPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ['photo']


class ProductSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['size']


class ProductColorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['color']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer()
    photos = ProductPhotoSerializer(many=True)
    size = ProductSizeSerializer(many=True)
    color = ProductColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name', 'slug', 'category', 'description', "image", 'price', 'available',
                  'created', 'updated', 'photos', 'size', 'color']
