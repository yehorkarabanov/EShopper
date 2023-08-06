from django.shortcuts import render
from .models import Category, Product


def home(request):
    products = Product.objects.all().order_by('-updated')
    categories = Category.objects.all()
    categories_with_images = [category for category in categories if category.image]
    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'page': 'home',
                                              'category_img': categories_with_images})
