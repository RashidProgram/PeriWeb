from django.urls import path
from .views import UserCreateView, logout_view
from django.contrib.auth.views import LoginView
from django.conf.urls import static
from django11 import settings
app_name = 'users'

urlpatterns = [
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]

if settings.DEBUG:
    urlpatterns = static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

