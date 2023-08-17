from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import View
from shop.models import Product, Category
from .cart import Cart
from utils.ajax import is_ajax
from django.template.loader import render_to_string


class CartActionsView(View):
    def get(self, request):
        return render(request, 'cart/cart_detail.html')

    def post(self, request, action):
        product_id = request.POST.get('product_id')
        color = request.POST.get('color')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))
        if not product_id or not color or not size:
            return HttpResponse('error in GET')

        product = get_object_or_404(Product, id=product_id, size__size=size, color__color=color)
        if not product:
            return HttpResponse('error in Product')

        cart = Cart(request)
        if action == 'add':
            cart.add(product, color, size, quantity)
            return HttpResponse('success')
        elif action == 'delete':
            cart.remove(product, color, size)
            return HttpResponse('success')

        return HttpResponse('error in other')
