# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-13 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ['nome'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AddField(
            model_name='produto',
            name='grama',
            field=models.CharField(default=0, max_length=4, verbose_name='Grama'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=20, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero',
            field=models.CharField(max_length=3, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descrição do alimento'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.CharField(max_length=10, verbose_name='Preço'),
        ),
    ]
