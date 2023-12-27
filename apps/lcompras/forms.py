# apps / lcompras / forms.py 
from django import forms
from apps.lcompras.models import Lcompras

# input("Estou em apps / lcompras / forms.py")

class LcomprasForms(forms.ModelForm):
    class Meta:
        model = Lcompras
        exclude = []
        labels = {
            'nome':'Produto',
            'unidade':'Unidade',
            'setor':'Setor',
            'codsetor':'Código Setor',
            'preco':'Preço',
            'foto':'Imagem',
            'observacao': 'Observação',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'unidade': forms.TextInput(attrs={'class':'form-control'}),
            'setor': forms.Select(attrs={'class':'form-control'}),
            'codsetor': forms.TextInput(attrs={'class':'form-control'}),
            'preco': forms.NumberInput(attrs={'class':'form-control'}),
            'foto': forms.FileInput(attrs={'class':'form-control'}),
            'observacao': forms.Textarea(attrs={'class':'form-control'}),
        }
