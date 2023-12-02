from django.db import models

OPCOES_SETORES = [
    ("Açougue", "Açougue"),
    ("Bebidas", "Bebidas"),
    ("Bomboniere", "Bomboniere"),
    ("Conservas", "Conservas"),
    ("Grãos", "Grãos"),
    ("Higiene", "Higiene"),
    ("Hortifruti", "Hortifruti"),
    ("Laticínios", "Laticínios"),
    ("Organizadores", "Organizadores"),
    ("Padaria", "Padaria"),
]

class ProdutoImg(models.Model): 
    nome = models.CharField(max_length=30, null=False, blank=False)
    unidade = models.CharField(max_length=3)
    setor = models.CharField(max_length=15, choices=OPCOES_SETORES, default='')
    preco = models.FloatField()
    foto = models.ImageField(upload_to="fotos/", blank=True)

# função que devolve o nome de cada um dos itens
    def __str__(self):
        return self.nome