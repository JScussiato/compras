# apps / usuarios / forms.py
from django import forms

class LoginForms(forms.Form): # criando formulário em forms.py, desobriga a maioria dos códigos HTML respectivos
    nome_login=forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=30,
        widget=forms.TextInput( # widget permite se editar algumas características do input
            attrs={ # define um dicionário para estilização dos itens
                'class': 'form-control',
                # class é a chave/key e form-control é o valor, que é o que realmente vai formatar os estilos   
                'placeholder': 'Ex.: José dos Anzóis',
            }
        )
    )
    senha=forms.CharField(
        label='Senha',
        required=True,
        max_length=30,
        widget=forms.PasswordInput( # widget permite se editar algumas características do input
            attrs={ # define um dicionário para estilização dos itens
                'class': 'form-control',
                # class é a chave/key e form-control é o valor, que é o que realmente vai formatar os estilos
                'placeholder': 'Digite sua senha',
            }
        ),
    )

class CadastroForms(forms.Form): # o Forms de CadastroForms é apenas uma boa prática de programação
    nome_cadastro=forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={ 
                'class': 'form-control',
                'placeholder': 'Ex.: José dos Anzóis',
            }
        )
    )
    email=forms.EmailField(
        label='Email',
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs={ 
                'class': 'form-control',
                'placeholder': 'Ex.: jose@dosanzois.com',
            }
        )
    )
    senha_1=forms.CharField(
        label='Senha',
        required=True,
        max_length=10,
        widget=forms.PasswordInput(
            attrs={ 
                'class': 'form-control',
                'placeholder': 'Informe sua senha',
            }
        ),
    )
    senha_2=forms.CharField(
        label='Confirme a Senha',
        required=True,
        max_length=10,
        widget=forms.PasswordInput(
            attrs={ 
                'class': 'form-control',
                'placeholder': 'Confirme sua senha',
            }
        ),
    )

    def clean_nome_cadastro(self): # clean é comando e nome_cadastro é o nome do usuário 
        nome = self.cleaned_data.get('nome_cadastro')
        if nome: # valida se existe algo dentro de nome
            nome = nome.strip() # strip elimina espaços antes e depois da string recebida
            if ' ' in nome: # testa se existe espaço em branco dentro da string
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2