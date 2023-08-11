from django.conf import settings
from shop.models import Product


class Like:
    def __init__(self, request):
        self.session = request.session
        like = self.session.get(settings.LIKE_SESSION_ID)
        if not like:
            like = self.session[settings.LIKE_SESSION_ID] = []
        self.like = like

    def add(self, product):
        product_id = product.id
        if product_id not in self.like:
            self.like.append(product_id)
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = product.id
        if product_id in self.like:
            self.like.remove(product_id)
            self.save()

    def __iter__(self):
        print(self.like)
        product_ids = self.like
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            yield product

    def __len__(self):
        return len(self.like)

    def clear(self):
        del self.session[settings.LIKE_SESSION_ID]
        self.save()

    def __contains__(self, item):
        return item in self.like
