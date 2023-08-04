from django.shortcuts import render
from .models import Category, Product


def home(request):
    products = Product.objects.all().order_by('-updated')[:8]
    categories = Category.objects.all()[:10]
    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'page': 'home'})
