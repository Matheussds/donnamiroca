# Generated by Django 3.1 on 2020-08-12 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donnamirocagerencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MateriaPrima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7)),
                ('unidade_medida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donnamirocagerencia.unidademedida')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialFornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donnamirocagerencia.fornecedor')),
                ('materia_prima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donnamirocagerencia.materiaprima')),
            ],
        ),
    ]
