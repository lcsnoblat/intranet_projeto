# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-12 08:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0021_auto_20170708_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='fase',
            field=models.CharField(choices=[('Análise de Causa-Raiz', 'Análise de Causa-Raiz'), ('Tratamento Preliminar', 'Tratamento Preliminar'), ('Tratamento Definitivo', 'Tratamento Definitivo'), ('Análise de Procedência', 'Análise De Procedência'), ('Validação do Gestor', 'Validação do Gestor')], default='Análise de Causa-Raiz', max_length=50),
        ),
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 12, 6, 23, 57, 702002), '1 Dia'), (datetime.datetime(2017, 7, 15, 5, 23, 57, 702002), '3 Dias'), (datetime.datetime(2017, 7, 17, 5, 23, 57, 702002), '5 Dias')]),
        ),
    ]
