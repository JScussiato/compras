# apps / produtos / urls.py 
from django.urls import path
from apps.produtos.views import \
    indexprodutos, imagemprodutos, buscarproduto, novoproduto, editarproduto, deletarproduto, filtro
    # todos itens acima Vêm de views.py 

# input("Estou em apps / produtos / urls.py")

urlpatterns = [
    path('indexprodutos', indexprodutos, name='indexprodutos'), 
    # a declaração '' (vazio) é para que não seja exibido nada na URL
    path('imagemprodutos/<int:produto_id>', imagemprodutos, name='imagemprodutos'),
    path("buscarproduto", buscarproduto, name="buscarproduto"),
    path("novoproduto", novoproduto, name="novoproduto"),
    path("editarproduto/<int:produto_id>", editarproduto, name="editarproduto"),
    path("deletarproduto/<int:produto_id>", deletarproduto, name="deletarproduto"),
    path("filtro/<str:setor>", filtro, name="filtro"),
]
# 'imagemprodutos/' é o caminho a visualizar, e inclusive vai aparecer na url
# imagemprodutos é o template a renderizar
# o name é para usar url dinâmica no html, de <a href="imagemprodutos.html"> para <a href="{% url 'imagemprodutos' %}">
