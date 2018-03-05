from django.contrib import admin
from django.urls import path, include
from pages.views import home, pages
from news.views import news_list
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', home, name='home'),
    path('<slug:slug>', pages, name='pages'),
    path('news/', news_list, name='news_list'),
    path('news/<int:article_id>', news_list, name='news_detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
