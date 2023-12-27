# apps / produtos / models.py 
from django.db import models

# input("Estou em apps / produtos / models.py")

OPCOES_SETOR = [
    ("Conservas","Conservas"),
    ("Graos","Grãos"),
    ("Bomboniere","Bomboniére"),
    ("Acougue","Açougue"),
    ("Limpeza","Limpeza"),
    ("Organizadores","Organizadores"),
    ("Hortifruti","Hortifruti"),
    ("Padaria","Padaria"),
    ("Laticinios","Laticínios"),
    ("Bebidas","Bebidas"),
]

class ProdutoImg(models.Model): 
    nome = models.CharField(max_length=30, null=False, blank=False)
    unidade = models.CharField(max_length=3, null=True, blank=True)
    setor = models.CharField(max_length=15, choices=OPCOES_SETOR, default='')
    codsetor = models.CharField(max_length=2, editable=False, default='')
    preco = models.FloatField()
    foto = models.ImageField(upload_to="fotos/", blank=True)

# função que devolve o nome de cada um dos itens.
    def __str__(self):
        return self.nome