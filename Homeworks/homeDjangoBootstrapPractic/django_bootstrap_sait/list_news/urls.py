from django.urls import path, include
from .views import list_news, detail_news
app_name = "news"


urlpatterns = [
    path('list', list_news, name="list"),
    path('detail', detail_news, name="detail"),
]

