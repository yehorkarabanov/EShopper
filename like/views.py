from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from shop.models import Product, Category
from .like import Like
from utils.ajax import is_ajax


class LikeActionsView(View):
    def get(self, request):
        if is_ajax(request):
            pass
        categories = Category.objects.all()
        return render(request, 'like/like_detail.html')

    def post(self, request, action):
        product_id = request.POST.get('product_id')
        if product_id:
            like = Like(request)
            product = get_object_or_404(Product, id=product_id)
            if action == 'add':
                like.add(product)
            elif action == 'delete':
                like.remove(product)
            return HttpResponse('success')
        return HttpResponse('error')
