from .models import UnidadeMedida, MateriaPrima, MaterialFornecedor, Fornecedor
from django import forms


class MateriaPrimaForm(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    unidade_medida = forms.ModelChoiceField(label='Unidade de Medida', queryset=UnidadeMedida.objects.all().order_by('id'), widget=forms.Select(
        attrs={'id': 'unidade_m', 'onchange': 'valorUnidade()'}))
    quantidade = forms.FloatField(label='Quantidade', widget=forms.TextInput(
        attrs={'id': 'quantidade_m', 'onkeyup': 'valorUnidade()'}))
    valor = forms.DecimalField(label='Valor da Unidade R$', widget=forms.TextInput(
        attrs={'id': 'valor_unidade_m', 'class': 'v_unidade', 'onkeyup': 'valorPacote()'}))
    fornecedor = forms.ModelChoiceField(
        label='fornecedor', queryset=Fornecedor.objects.all().order_by('id'), widget=forms.Select)

    class Meta:
        model = MateriaPrima
        fields = ['nome', 'unidade_medida', 'quantidade', 'valor']


class MaterialFornecedorForm(forms.ModelForm):

    class Meta:
        model = MaterialFornecedor
        fields = ['fornecedor']


class FornecedorForm(forms.ModelForm):
    nome = forms.CharField(label='Nome')
    telefone = forms.CharField(
        label='Telefone', widget=forms.TextInput(attrs={'class': 'v_telefone'}))
    endereco = forms.CharField(label='Endereço')
    email = forms.CharField(label='Email')

    class Meta:
        model = Fornecedor
        fields = ['nome', 'telefone', 'endereco', 'email']
