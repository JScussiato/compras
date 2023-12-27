# apps / lcompras / admin.py 
from django.contrib import admin
from apps.lcompras.models import Lcompras

# input("Estou em apps / lcompras / admin.py")

class ListandoLcompras(admin.ModelAdmin): # modifica a forma de exibição do Django Admin
    list_display = ("id", "nome", "unidade", "codsetor", "setor", "preco", "foto", "observacao") 
    # define o que deve ser exibido
    list_display_links = ("id", "nome", "foto") # define os campos com link
    search_fields = ("nome", ) # define o campo de busca. TEM QUE ser uma Tupla!
    list_filter = ("setor", ) # define filtro. TEM QUE ser uma Tupla!
    list_per_page = 10 # define quantidade de registros exibidos por página

admin.site.register(Lcompras, ListandoLcompras) # Produto é o módulo que faz a "ponte" com o BD
