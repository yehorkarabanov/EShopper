from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('detail/', views.AccountDetailView.as_view(), name='detail'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
]
