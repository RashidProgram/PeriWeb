from .models import Product, Catalog
from django.shortcuts import render


def catalogs(request):
    catalogs_list = Catalog.objects.all()
    return render(request, 'products/catalogs.html', {"catalogs": catalogs_list})


def list_products(request, catalog_title):
    products_list = Product.objects.all()
    return render(request, 'products/product_list.html', {"products": products_list, "title": catalog_title})


def detail_product(request, this_id):
    product_detail = Product.objects.get(id=this_id)
    return render(request, 'products/product_detail.html', {"product": product_detail, "title": this_id})
