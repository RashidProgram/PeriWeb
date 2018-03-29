from django.shortcuts import render
from .models import Product
from django.utils import timezone


def index(request):
    context = {
        'all_products': Product.objects.all(),
        'count': Product.objects.count(),
        'yagodi': Product.objects.filter(catalog__title__icontains="Ягоды"),
        'fructi_ovoshi': Product.objects.filter(catalog__title__in=["Фрукты", "Овощи"]),
        'big_10': Product.objects.filter(count__gt=10),
        'small_10': Product.objects.filter(count__lt=10),
        'import': Product.objects.filter(is_import__exact=True),
        'local': Product.objects.filter(is_import__exact=False),
        'prosroch': Product.objects.filter(shelf_life__lt=timezone.now()),
        'apple': Product.objects.filter(title__icontains="Яблоки"),
        'notApple': Product.objects.exclude(title__icontains="Яблоки"),
        'sort_fructs': Product.objects.filter(catalog__title__icontains="Фрукты").order_by('title'),
    }
    return render(request, 'index.html', context)

