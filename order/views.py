from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreatedForm
from cart.cart import Cart
from django.views import View
from shop.models import ProductSize, ProductColor


class CreateOrder(View):
    def get(self, request):
        form = OrderCreatedForm()
        return render(request, 'order/create.html', {'form': form, })

    def post(self, request):
        form = OrderCreatedForm(request.POST)
        if form.is_valid():
            cart = Cart(request)
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                    color=ProductColor.objects.get(color=item['color']),
                    size=ProductSize.objects.get(size=item['size'])
                )
            cart.clear()
            return render(request, 'order/created.html', {'order': order, })
        return render(request, 'order/create.html', {'form': form, })
