from rest_framework import viewsets
from order.models import Order, OrderItem
from .serializers import OrderSerializer
from rest_framework.permissions import AllowAny


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
