# apps / produtos / apps.py 
from django.apps import AppConfig

# input("Estou em apps / produtos / apps.py")

class ProdutosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.produtos"
