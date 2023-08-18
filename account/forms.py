from django import forms
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists. Please use a different email")
        return email
