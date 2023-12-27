# apps / lcompras / urls.py 
from django.urls import path
from apps.lcompras.views import \
    indexlcompras, imagemlcompras, novoitemlcompras, deletarlcompras, deletaritemlcompras, buscarlcompras, \
    editarlcompras, filtrolcompras

# input("Estou em apps / lcompras / urls.py")

urlpatterns = [
    path('', indexlcompras, name='indexlcompras'), 
    path('imagemlcompras/<int:lcompras_id>', imagemlcompras, name='imagemlcompras'),
    path("buscarlcompras", buscarlcompras, name="buscarlcompras"),
    path('novoitemlcompras', novoitemlcompras, name='novoitemlcompras'), 
    path("editarlcompras/<int:lcompras_id>", editarlcompras, name="editarlcompras"),
    path('deletarlcompras', deletarlcompras, name='deletarlcompras'), 
    path('deletaritemlcompras/<int:lcompras_id>', deletaritemlcompras, name='deletaritemlcompras'), 
    path("filtrolcompras/<str:setor>", filtrolcompras, name="filtrolcompras"),
]
