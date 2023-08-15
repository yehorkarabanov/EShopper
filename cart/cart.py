from decimal import Decimal
from django.conf import settings
from shop.models import Product
from django.db.models import Q


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, color, size, quantity=1):
        cur_product_id = f"{str(product.id)}-{str(size)}-{str(color)}"
        if cur_product_id not in self.cart:
            self.cart[cur_product_id] = {'quantity': 0,
                                         'price': str(product.price)}
        self.cart[cur_product_id]['quantity'] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product, color, size):
        cur_product_id = f"{str(product.id)}-{str(size)}-{str(color)}"
        if cur_product_id in self.cart:
            del self.cart[cur_product_id]
            self.save()

    def __iter__(self):
        cur_product_ids = self.cart.keys()
        product_ids = [s.split('-') for s in cur_product_ids]
        sizes = [item[1] for item in product_ids]
        colors = [item[2] for item in product_ids]
        product_ids = [item[0] for item in product_ids]

        products = []
        for product_id in product_ids:
            products += Product.objects.filter(id=product_id)

        cart = self.cart.copy()
        for index, product in enumerate(products):
            cart[f"{str(product.id)}-{str(sizes[index])}-{str(colors[index])}"]['product'] = product
        for item, color, size in zip(cart.values(), colors, sizes):
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            item['color'] = color
            item['size'] = size
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def __contains__(self, item):
        return item in self.cart
