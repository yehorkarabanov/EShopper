from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.ProductsListView.as_view(), name='products_list'),
    path('shop/<slug:category_slug>/', views.ProductsListView.as_view(), name='products_list_by_category'),
    path('detail/<int:pk>/<slug:product_slug>/', views.ProductDetailView.as_view(), name='product_detail_view'),
    path('api/', include('shop.api.urls')),
]