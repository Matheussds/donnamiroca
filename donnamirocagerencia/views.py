from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UnidadeMedida, MateriaPrima, MaterialFornecedor, Fornecedor
from .form import FornecedorForm, MateriaPrimaForm, MaterialFornecedorForm


def materia_prima(request):
    data = {}
    data['materia_prima'] = MateriaPrimaForm(request.POST or None)
    data['material_fornecedor'] = MaterialFornecedorForm(request.POST or None)

    if data['materia_prima'].is_valid():
        materiaprima = data['materia_prima'].save()
        id = materiaprima.id
        if data['material_fornedor'].is_valid():
            material_fornecedor = data['material_fornecedor']
            material_fornecedor.materia_prima = id
            materiaprima.save()
            material_fornecedor.save()
            return redirect('url_materia_prima')

    data['materiasprimas'] = MateriaPrima.objects.all()
    data['unidadesmedidas'] = UnidadeMedida.objects.all()
    return render(request, 'donnamirocagerencia/material/materia_prima.html', data)


def producao(request):
    return render(request, 'donnamirocagerencia/produto/produção.html')


def index(request):
    return render(request, 'donnamirocagerencia/index/index.html')


def fornecedor(request):
    data = {}
    form = FornecedorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_fornecedor')

    data['fornecedores'] = Fornecedor.objects.all()
    data['form'] = form
    return render(request, 'donnamirocagerencia/fornecedor/fornecedor.html', data)
