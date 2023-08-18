from django.db import models
from shop.models import Product, ProductSize, ProductColor
from account.models import UserAccount


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(UserAccount, related_name='orders', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f"Order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    color = models.ForeignKey(ProductColor, related_name='order_item_color', on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, related_name='order_item_size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{str(self.id)}-{str(self.size.size)}-{str(self.color.color)}"

    def get_cost(self):
        return self.price * self.quantity
