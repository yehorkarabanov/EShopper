from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'product_size', views.ProductSizeViewSet, basename='product_size')
router.register(r'product_color', views.ProductColorViewSet, basename='product_color')

urlpatterns = router.urls
