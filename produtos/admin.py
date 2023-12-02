from django.contrib import admin
from produtos.models import ProdutoImg

class ListandoProdutos(admin.ModelAdmin): # modifica a forma de exibição do Django Admin
    list_display = ("id", "nome", "unidade", "setor", "preco", "foto") # define o que deve ser exibido
    list_display_links = ("id", "nome", "foto") # define os campos com link
    search_fields = ("nome", ) # define o campo de busca. TEM QUE ser uma Tupla!
    list_filter = ("setor", ) # define filtro. TEM QUE ser uma Tupla!
    list_per_page = 10 # define quantidade de registros exibidos por página

admin.site.register(ProdutoImg, ListandoProdutos) # Produto é o módulo que faz a "ponte" com o BD