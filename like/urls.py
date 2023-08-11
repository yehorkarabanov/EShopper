from django.urls import path
from . import views

app_name = 'like'

urlpatterns = [
    path('', views.LikeActionsView.as_view(), name='like_detail'),
    path('add/', views.LikeActionsView.as_view(), {'action': 'add'}, name='like_add'),
    path('delete/', views.LikeActionsView.as_view(), {'action': 'delete'}, name='like_delete'),
]
