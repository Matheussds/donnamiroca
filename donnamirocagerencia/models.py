from django.db import models

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=15)

    class Meta():
        verbose_name_plural = 'UnidadesMedidas'

    def __str__(self):
        return self.nome


class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(null=True, blank=True, max_length=15)
    email = models.EmailField(null=True, blank=True, max_length=254)
    endereco = models.CharField(null=True, blank=True, max_length=254)

    class Meta():
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome


class MateriaPrima(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.FloatField(max_length=7)
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'MateriasPrimas'

    def __str__(self):
        return self.nome


class MaterialFornecedor(models.Model):
    materia_prima = models.ForeignKey(MateriaPrima, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'MateriaisFornecedores'
