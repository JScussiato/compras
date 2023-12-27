# apps / cargajson / urls.py 
from django.urls import path
from apps.cargajson.views import importar_dados

urlpatterns = [
    path('importar_dados', importar_dados, name='importar_dados'),
]
