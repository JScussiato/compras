from django.urls import path
from produtos.views import indexprodutos, imagemprodutos, buscarproduto # Vêm de views.py

urlpatterns = [
    path('', indexprodutos, name='indexprodutos'),
    path('imagemprodutos/<int:foto_id>', imagemprodutos, name='imagemprodutos'),
    path("buscarproduto", buscarproduto, name="buscarproduto"),
]
# 'imagemprodutos/' é o caminho a visualizar
# imagemprodutos é o template a renderizar
# o name é para usar url dinâmica no html, de <a href="imagemprodutos.html"> para <a href="{% url 'imagemprodutos' %}">
