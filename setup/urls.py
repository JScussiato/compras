""" URL configuration for setup project."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('apps.produtos.urls')),
    path('', include('apps.usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# o + static acima, indica ao Django que tem que usar estas referências
