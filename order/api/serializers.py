from rest_framework import serializers
from order.models import Order, OrderItem


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    color = serializers.CharField(source='color.color')
    size = serializers.CharField(source='size.size')
    product_name = serializers.CharField(source='product.name')
    product_id = serializers.IntegerField(source='product.pk')

    class Meta:
        model = OrderItem
        fields = ['price', 'quantity', 'color', 'size', 'product_name', 'product_id']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    total_cost = serializers.DecimalField(source='get_total_cost', max_digits=10, decimal_places=2)
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'city', 'state', 'postal_code',
                  'created', 'updated', 'paid', 'total_cost', 'items']
