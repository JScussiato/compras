# apps / cargajson / admin.py 
from django.contrib import admin
from apps.cargajson.models import CargajsonImg

class ListandoCarga(admin.ModelAdmin):
    pass
    # list_display = ("id", "nome", "unidade", "setor", "preco", "foto")
    # list_display_links = ("id", "nome", "foto")
    # search_fields = ("nome", )
    # list_filter = ("setor", )
    # list_per_page = 10

admin.site.register(CargajsonImg, ListandoCarga) 