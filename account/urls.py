from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('detail/', views.AccountDetailView.as_view(), name='detail'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('user_change/', views.UserDataChange.as_view(), name='user_data_change'),
]
