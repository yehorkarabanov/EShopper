from django.urls import path, include
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.CreateOrder.as_view(), name='create'),
    path('api/', include('order.api.urls')),
]
