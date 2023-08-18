from django.contrib import admin
from .models import UserAccount
from order.models import Order


class OrderInline(admin.StackedInline):
    model = Order
    extra = 0


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_id', 'get_user_name', 'get_orders_ids']
    inlines = [OrderInline]

    def get_user_name(self, obj):
        return obj.user.username

    get_user_name.short_description = 'Username'

    def get_user_id(self, obj):
        return obj.user.id

    get_user_name.short_description = 'User ID'

    def get_orders_ids(self, obj):
        list = []
        for order in obj.orders.all():
            list.append(order.id)
        return list

    get_orders_ids.short_description = 'Orders IDs'
