
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path , include
from django.shortcuts import render

from .views import index , blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)