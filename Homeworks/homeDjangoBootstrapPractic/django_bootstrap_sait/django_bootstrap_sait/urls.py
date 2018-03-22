from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import list_news.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('news/', include(list_news.urls, namespace='news',))
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
