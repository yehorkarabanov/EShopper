from django import forms
from .models import Order


class OrderCreatedForm(forms.ModelForm):
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address_1', 'address_2', 'country', 'city',
                  'state', 'postal_code']

    def save(self, commit=True):
        self.instance.address = f"{self.cleaned_data['address_1']} {self.cleaned_data['address_2']}"
        return super().save(commit=commit)

    def __init__(self, *args, **kwargs):
        super(OrderCreatedForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        self.fields['first_name'].widget.attrs.update({'placeholder': 'John'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Doe'})
        self.fields['email'].widget.attrs.update({'placeholder': 'johndoe@example.com'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': '+15551234567'})
        self.fields['address_1'].widget.attrs.update({'placeholder': '123 Main St'})
        self.fields['address_2'].widget.attrs.update({'placeholder': 'Apt 4B'})
        self.fields['country'].widget.attrs.update({'placeholder': 'United States'})
        self.fields['city'].widget.attrs.update({'placeholder': 'New York'})
        self.fields['state'].widget.attrs.update({'placeholder': 'New York'})
        self.fields['postal_code'].widget.attrs.update({'placeholder': '10001'})
