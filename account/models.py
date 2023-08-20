from django.db import models
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    phone_number = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=250, blank=True)
