from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView


def home(request):
    products = Product.objects.all().order_by('-updated')
    categories = Category.objects.all()
    categories_with_images = [category for category in categories if category.image]
    return render(request, 'shop/home.html', {'categories': categories, 'products': products, 'page': 'home',
                                              'category_img': categories_with_images})


class ProductsListView(ListView):
    model = Product
    template_name = 'shop/list.html'
    queryset = Product.objects.all()
    paginate_by = 1

    def get_queryset(self):
        category_slug = self.kwargs.get('categoty_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            return Product.objects.filter(category=category)
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['recommended_products'] = Product.objects.all()[:5]
        return context