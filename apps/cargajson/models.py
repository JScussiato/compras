# apps / cargajson / models.py 
from django.db import models

class CargajsonImg(models.Model): 
    nome = models.CharField(max_length=30, null=False, blank=False)
    unidade = models.CharField(max_length=3)
    setor = models.IntegerField()
    preco = models.FloatField()
    foto = models.ImageField(upload_to="fotos/", blank=True)

    def __str__(self):
        return self.nome
