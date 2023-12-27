# apps / lcompras / views.py 
from django.shortcuts import render, get_object_or_404, redirect
from apps.lcompras.models import Lcompras
from apps.lcompras.forms import LcomprasForms
from django.contrib import messages
from django.core.paginator import Paginator #, EmptyPage, PageNotAnInteger

# input("Estou em apps / lcompras / views.py")

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

def indexlcompras(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')
	lcompras = Lcompras.objects.order_by("codsetor", "nome").all() # o modelo busca tudo que tem no BD
	paginator = Paginator(lcompras, 4)
	page = request.GET.get('page')
	lcompras_por_pagina = paginator.get_page(page)
	return render(request, 'lcompras/indexlcompras.html', {"cards": lcompras_por_pagina}) 
	# cards envia o dicionário p/o render

def imagemlcompras(request, lcompras_id): 
	lcompras = get_object_or_404(Lcompras, pk=lcompras_id) 
			# este comando busca o objeto  no BD
			# já o get_object_or_404 controla se acha ou não o registro
	return render(request, 'lcompras/imagemlcompras.html', {"lcompras": lcompras}) 
			# acima está sendo passado para o HTML o objeto que faz referência ao ID que está sendo processado
			# o 1º request (def) recebe a requisição
			# o 2º request (render) devolve a requisição
			# lcompras/imagemlcompras.html é a tela a renderizar

def buscarlcompras(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')

	lcompras = Lcompras.objects.order_by("codsetor", "nome").all()
	if "buscarlcompras" in request.GET: # confirma que o termo buscarlcompras está contido na URL
		lcompras_a_buscar = request.GET['buscarlcompras'] # o 'buscarlcompras' é o "name" colocado no _menu.html
		if lcompras_a_buscar: # ou seja, se há conteúdo
			lcompras = lcompras.filter(nome__icontains=lcompras_a_buscar) 
			# redefine lcompras e aplica filtro
			# nome__icontains identifica se lcompras_a_buscar contém alguma referência à palavra que está sendo buscada, o que não precisa ser exatamente igual, mas podendo conter parte para dar match

	return render(request, "lcompras/indexlcompras.html", {"cards": lcompras}) 
# recebe e devolve a requisição, e também a página a renderizar

def novoitemlcompras(request):
	if not request.user.is_authenticated:
		messages.error(request, "Usuário não logado")
		return redirect('login')
	form = LcomprasForms
	if request.method == 'POST':
		form = LcomprasForms(request.POST, request.FILES)
		if form.is_valid():
			setor_selecionado = form.cleaned_data['setor']
			for chave, valor in DIC_SETORES.items():
				if chave == setor_selecionado:
					break
			if Lcompras.objects.filter(nome=form.cleaned_data['nome']).exists():
				messages.error(request, 'Item já existe')
			else:
				form.save(commit=False)
				form.instance.codsetor = valor
				form.save() # salva no BD
				messages.success(request, 'Novo Item Cadastrado')
			return redirect('indexlcompras')
	return render(request, 'lcompras/novoitemlcompras.html', {'form': form}) 
	# form passa o formulário para o template

def editarlcompras(request, lcompras_id):
	lcompras = Lcompras.objects.get(id=lcompras_id) 
	# busca no BD. Lcompras é a instanciação do BD. lcompras_id vem do path editarlcompras de urls.py 
	form = LcomprasForms(instance=lcompras) # aqui coloca os dados que vieram do banco dentro do formulário
	setor_anterior = lcompras.setor
	if request.method == 'POST':
		form = LcomprasForms(request.POST, request.FILES, instance=lcompras) 
		# o instance faz com que o que não seja modificado, permaneça com os dados que foram buscados no BD
		if form.is_valid():
			if form.cleaned_data['setor'] != setor_anterior:
				for chave, valor in DIC_SETORES.items():
					if chave == form.cleaned_data['setor']:
						form.instance.codsetor = valor
						break
			form.save(commit=False)
			form.save() # salva no BD
			messages.success(request, 'L.C. alterada com sucesso!')
			return redirect('indexlcompras')
	return render(request, 'lcompras/editarlcompras.html', {'form': form, 'lcompras_id': lcompras_id})

def deletarlcompras(request, lcompras_id):
	lcompras = Lcompras.objects.get(id=lcompras_id)
	lcompras.delete()
	messages.success(request, 'Item apagado com sucesso!')
	return redirect('indexlcompras')

def deletaritemlcompras(request, lcompras_id):
	lcompras = Lcompras.objects.get(id=lcompras_id)
	lcompras.delete()
	messages.success(request, 'Item da L.C. apagado com sucesso!')
	return redirect('indexlcompras')

def filtrolcompras(request, setor):
	lcompras = Lcompras.objects.order_by("codsetor", "nome").filter(setor=setor) 
# 	# o modelo busca tudo que tem no BD filtrado por setor  do BD igual ao setor que está sendo passada
	return render(request, 'lcompras/indexlcompras.html', {"cards": lcompras})