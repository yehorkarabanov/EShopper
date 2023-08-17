from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import View
from shop.models import Product
from .like import Like
from utils.ajax import is_ajax
from django.core.paginator import Paginator
from django.template.loader import render_to_string


class LikeActionsView(View):
    def get(self, request):
        like = Like(request)
        products = Product.objects.filter(id__in=like.like)
        items_per_page = 8
        paginator = Paginator(products, items_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if is_ajax(request):
            return HttpResponse(render_to_string('like/frames/like_list.html', {
                'page_obj': page_obj,
                'paginator': paginator,
                'is_paginated': paginator.num_pages > 1,
                'like': like,
            }))
        return render(request, 'like/like_detail.html', {
            'page_obj': page_obj,
            'paginator': paginator,
            'is_paginated': paginator.num_pages > 1,
        })

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
