# apps / cargajson / views.py 
from django.shortcuts import render #, get_object_or_404, redirect
from apps.cargajson.models import CargajsonImg #, CargajsonImgModel
from django.contrib import messages
from tablib import Dataset

def importar_dados(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_data = request.FILES['cargajson']
        if not new_data.name.endswith('.json'):
            messages.error(request, 'Formato de arquivo inválido. Por favor, envie um arquivo JSON.')
        else:
            imported_data = dataset.load(new_data.read().decode('utf-8'), format='json')
            model = CargajsonImg()
            result = model.import_data(dataset, dry_run=True) 
            if not result.has_errors():
                model.import_data(dataset, dry_run=False)
                messages.success(request, 'Dados importados com sucesso!')
            else:
                messages.error(request, 'Ocorreu um erro ao importar os dados.')
    return render(request, 'cargajson/importar_dados.html')
