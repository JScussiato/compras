# apps / usuarios / urls.py
from django.urls import path
from apps.usuarios.views import login, cadastro, logout # Vem de views.py

urlpatterns = [
    path('login', login, name="login"),
    path('cadastro', cadastro, name="cadastro"),
    path('logout', logout, name="logout"),
]
