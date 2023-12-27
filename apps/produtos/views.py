# apps / produtos / views.py 
from django.shortcuts import render, get_object_or_404, redirect
from apps.produtos.models import ProdutoImg
from apps.produtos.forms import ProdutoForms
from django.contrib import messages
from django.core.paginator import Paginator

# input("Estou em apps / produtos / views.py")

DIC_SETORES = {
	'Conservas':1, 
	'Graos':2, 
	'Bomboniere':3, 
	'Acougue':4, 
	'Limpeza':5, 
	'Organizadores':6, 
	'Hortifruti':7, 
	'Padaria':8, 
	'Laticinios':9, 
	'Bebidas':10, 	
}

def indexprodutos(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')
	produtos = ProdutoImg.objects.order_by("codsetor","nome").all() # o modelo busca tudo que tem no BD
	paginator = Paginator(produtos, 6)
	page = request.GET.get('page')
	produtos_por_pagina = paginator.get_page(page)
	return render(request, 'produtos/indexprodutos.html', {"cards": produtos_por_pagina}) # cards envia o dicionário p/o render

def imagemprodutos(request, produto_id): 
	produto = get_object_or_404(ProdutoImg, pk=produto_id) 
	# este comando busca o objeto  no BD
	# já o get_object_or_404 controla se acha ou não o registro
	return render(request, 'produtos/imagemprodutos.html', {"produto": produto}) 
	# acima está sendo passado para o HTML o objeto que faz referência ao ID que está sendo processado
	# o 1º request (def) recebe a requisição
	# o 2º request (return) devolve a requisição
	# produtos/imagemprodutos.html é a tela a renderizar

def buscarproduto(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')

	produtos = ProdutoImg.objects.order_by("codsetor", "nome").all()
	if "buscarproduto" in request.GET: # confirma que o termo buscarproduto está contido na URL
		produto_a_buscar = request.GET['buscarproduto'] # o 'buscarproduto' é o "name" colocado no _menu.html
		if produto_a_buscar: # ou seja, se há conteúdo
			produtos = produtos.filter(nome__icontains=produto_a_buscar) 
			# redefine produto e aplica filtro
			# nome__icontains identifica se produto_a_buscar contém alguma referência à palavra que está sendo buscada, o que não precisa ser exatamente igual, mas podendo conter parte para dar match

	return render(request, "produtos/indexprodutos.html", {"cards": produtos}) 
# recebe e devolve a requisição, e também a página a renderizar

def novoproduto(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')
	form = ProdutoForms # instancia o formulário
	if request.method == 'POST':
		form = ProdutoForms(request.POST, request.FILES) 
		# instancia novo formulário, passando para dentro o que veio pelo POST
		# request.FILES faz com que apanhe os arquivos que estão sendo enviados
		if form.is_valid():
			setor_selecionado = form.cleaned_data['setor']
			for chave, valor in DIC_SETORES.items():
				if chave == setor_selecionado:
					break

			if ProdutoImg.objects.filter(nome=form.cleaned_data['nome']).exists():
				messages.error(request, 'Produto já existe')
			else:
				form.save(commit=False)
				form.instance.codsetor = valor
				form.save() # salva no BD
				messages.success(request, 'Novo produto cadastrado')
			return redirect('indexprodutos')
	return render(request, 'produtos/novoproduto.html', {'form': form}) # form passa o formulário para o template

def editarproduto(request, produto_id):
	produto = ProdutoImg.objects.get(id=produto_id) 
	setor_anterior = produto.setor
	# busca no BD. ProdutoImg é a instanciação do BD. produto_id vem do path editarproduto de urls.py 
	form = ProdutoForms(instance=produto) # aqui coloca os dados que vieram do banco dentro do formulário
	if request.method == 'POST':
		form = ProdutoForms(request.POST, request.FILES, instance=produto) 
		# o instance faz com que o que não seja modificado, permaneça com os dados que foram buscados no BD
		if form.is_valid():
			if form.cleaned_data['setor'] != setor_anterior:
				for chave, valor in DIC_SETORES.items():
					if chave == form.cleaned_data['setor']:
						form.instance.codsetor = valor
						break
			form.save(commit=False)
			form.save() # salva no BD
			messages.success(request, 'Produto alterado com sucesso!')
			return redirect('indexprodutos')
	return render(request, 'produtos/editarproduto.html', {'form': form, 'produto_id': produto_id})

def deletarproduto(request, produto_id):
	produto = ProdutoImg.objects.get(id=produto_id)
	produto.delete()
	messages.success(request, 'Produto apagado com sucesso!')
	return redirect('indexprodutos')

def filtro(request, setor):
	produtos = ProdutoImg.objects.order_by("codsetor", "nome").filter(setor=setor) 
	# o modelo busca tudo que tem no BD filtrado por setor  do BD igual ao setor que está sendo passada
	return render(request, 'produtos/indexprodutos.html', {"cards": produtos})