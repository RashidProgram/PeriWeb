from django.urls import path
from .views import catalogs, list_products, detail_product
app_name = 'products'

urlpatterns = [
    path('', catalogs, name='catalogs'),
    path('<slug:catalog_title>/', list_products, name='list'),
    path('detail/<int:this_id>/', detail_product, name='detail'),
]
