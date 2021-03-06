# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-12 21:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0002_interacao_data_interacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interacao',
            name='descricao',
            field=models.CharField(max_length=750, verbose_name='Faça uma BaseInteracao'),
        ),
        migrations.AlterField(
            model_name='interacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BaseInteracao_chamado', to=settings.AUTH_USER_MODEL),
        ),
    ]
