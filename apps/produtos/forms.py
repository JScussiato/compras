# apps / produtos / forms.py 
from django import forms
from apps.produtos.models import ProdutoImg

# input("Estou em apps / produtos / forms.py")

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = ProdutoImg
        exclude = []
        labels = {
            'nome':'Produto',
            'unidade':'Unidade',
            'codsetor':'Cód Setor',
            'setor':'Setor',
            'preco':'Preço',
            'foto':'Imagem',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}), # a class aqui é referente ao CSS
            'unidade': forms.TextInput(attrs={'class':'form-control'}),
            'codsetor': forms.NumberInput(attrs={'class':'form-control'}),
            'setor': forms.Select(attrs={'class':'form-control'}),
            'preco': forms.NumberInput(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
        }
