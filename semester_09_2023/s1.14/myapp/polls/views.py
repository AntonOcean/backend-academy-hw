from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from polls.models import Shop, Product


def index(request):
    return render(request, 'index.html', {})


def shop_list(request):
    products = Product.objects.all()

    context = {
        "shop_list": Shop.objects.all(),
        "product": {
            "title_x": [p.title for p in products],
            "price_y": [p.price for p in products]
        }
    }

    return render(request, 'shop/shops.html', context)
