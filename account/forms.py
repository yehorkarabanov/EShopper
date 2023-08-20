from django import forms
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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


class ExtendedUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = self.instance
        if User.objects.exclude(pk=user.pk).filter(email=email).exists():
            raise ValidationError("Email already exists. Please use a different email")
        return email


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['address', 'phone_number']
