from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.ProductsListView.as_view(), name='products_list'),
    path('shop/<slug:categoty_slug>/', views.ProductsListView.as_view(), name='products_list_by_category'),
]