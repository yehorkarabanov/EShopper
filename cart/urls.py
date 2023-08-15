from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartActionsView.as_view(), name='cart_detail'),
    path('add/', views.CartActionsView.as_view(), {'action': 'add'}, name='cart_add'),
    path('delete/', views.CartActionsView.as_view(), {'action': 'delete'}, name='cart_delete')
]