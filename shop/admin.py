from django.contrib import admin
from .models import Category, Product, ProductPhoto


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


class ProductPhotoInline(admin.StackedInline):
    model = ProductPhoto


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    inlines = [ProductPhotoInline]

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
