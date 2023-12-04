from django.shortcuts import render, get_object_or_404, redirect
from produtos.models import ProdutoImg
from django.contrib import messages

def indexprodutos(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')
	produtos = ProdutoImg.objects.order_by("nome").all() # o modelo busca tudo que tem no BD
	return render(request, 'produtos/indexprodutos.html', {"cards": produtos}) # cards envia o dicionário p/o render

def imagemprodutos(request, foto_id): 
	produto = get_object_or_404(ProdutoImg, pk=foto_id) 
	# este comando busca o objeto  no BD
	# já o get_object_or_404 controla se acha ou não o registro
	return render(request, 'produtos/imagemprodutos.html', {"produto": produto}) 
	# acima está sendo passado para o HTML o objeto que faz referência ao ID que está sendo processado

# o 1º request recebe a requisição
# o 2º request devolve a requisição
# produtos/imagemprodutos.html é a tela a renderizar

def buscarproduto(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')

	produtos = ProdutoImg.objects.order_by("nome").all()
	if "buscarproduto" in request.GET: # confirma que o termo buscarproduto está contido na URL
		produto_a_buscar = request.GET['buscarproduto'] # o 'buscarproduto' é o "name" colocado no _menu.html
		if produto_a_buscar: # ou seja, se há conteúdo
			produtos = produtos.filter(nome__icontains=produto_a_buscar) 
			# redefine produto e aplica filtro
			# nome__icontains identifica se produto_a_buscar contém alguma referência à palavra que está sendo buscada, o que não precisa ser exatamente igual, mas podendo conter parte para dar match

	return render(request, "produtos/buscarproduto.html", {"cards": produtos}) 
# recebe e devolve a requisição, e também a página a renderizar