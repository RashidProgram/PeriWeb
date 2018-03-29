from django.urls import path
from .views import NewsDetailView, NewsListView
app_name = "news"


urlpatterns = [
    path('list', NewsListView.as_view(), name="list"),
    path('detail/<int:kv>', NewsDetailView.as_view(), name="detail"),
]

