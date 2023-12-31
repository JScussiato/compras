# setup / urls.py
""" URL configuration for setup project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# input("Estou em setup / urls.py")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.lcompras.urls')),
    path('', include('apps.produtos.urls')),
    path('', include('apps.usuarios.urls')),
    path('', include('apps.cargajson.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
