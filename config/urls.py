from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home_page'),
    path('files',include('files.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)