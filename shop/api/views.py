from rest_framework import generics, viewsets
from rest_framework.response import Response
from shop.models import Product, Category, ProductColor, ProductSize
from shop.api.seializers import CategorySerializer, ProductSerializer, ProductColorSerializer, ProductSizeSerializer
from django.db.models import Q, Count


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductSizeViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSizeSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = ProductSize.objects.annotate(
                count=Count('products', filter=Q(products__category__pk=category_id))
            )
        else:
            queryset = ProductSize.objects.annotate(count=Count('products'))
        return queryset


class ProductColorViewSet(viewsets.ModelViewSet):
    serializer_class = ProductColorSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = ProductColor.objects.annotate(
                count=Count('products', filter=Q(products__category__pk=category_id))
            )
        else:
            queryset = ProductColor.objects.annotate(count=Count('products'))
        return queryset
