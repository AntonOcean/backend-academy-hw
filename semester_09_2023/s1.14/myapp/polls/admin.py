from django.contrib import admin

from .models import Shop, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    fields = ('shop', ('title', 'description', 'price'), 'rating')


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'email')
