# Generated by Django 5.1.3 on 2024-11-19 01:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('endereco', models.CharField(max_length=50)),
                ('data_inicio', models.DateField()),
                ('dt_prev_fim', models.DateField()),
                ('progresso_total', models.DecimalField(decimal_places=2, default=0, help_text='Progresso total da obra em %', max_digits=5)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, help_text='Valor total da obra', max_digits=10)),
                ('valor_gasto', models.DecimalField(decimal_places=2, default=0, help_text='Valor gasto em materiais', max_digits=10)),
                ('gerente', models.ForeignKey(limit_choices_to={'tipo_usuarios': 'gerente'}, on_delete=django.db.models.deletion.CASCADE, related_name='obras_gerenciadas', to='usuarios.perfil')),
                ('mestres', models.ManyToManyField(blank=True, limit_choices_to={'tipo_usuarios': 'mestre'}, related_name='obras_como_mestre', to='usuarios.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('quantidade', models.IntegerField(help_text='Quantidade comprada')),
                ('preco_total', models.DecimalField(decimal_places=2, help_text='Preço total do material', max_digits=10)),
                ('data_compra', models.DateField()),
                ('fornecedor', models.CharField(max_length=100)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materiais', to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_consumida', models.IntegerField(help_text='Quantidade consumida')),
                ('data_consumo', models.DateField(auto_now_add=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumos', to='obras.material')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consumos', to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('progresso', models.DecimalField(decimal_places=2, help_text='Progresso em %', max_digits=5)),
                ('mestre_responsavel', models.ForeignKey(limit_choices_to={'tipo_usuarios': 'mestre'}, on_delete=django.db.models.deletion.CASCADE, related_name='acompanhamentos', to='usuarios.perfil')),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acompanhamentos', to='obras.obra')),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('funcao', models.CharField(max_length=50)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('obra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profissionais', to='obras.obra')),
            ],
        ),
    ]
