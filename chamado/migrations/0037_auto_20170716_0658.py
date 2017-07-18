# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-16 09:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0036_auto_20170716_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_causa_raiz',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 6, 58, 37, 35135)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_procecencia',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 6, 58, 37, 35016)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_definitivo',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 6, 58, 37, 35077)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_preliminar',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 6, 58, 37, 35190)),
        ),
        migrations.AlterField(
            model_name='interacaoncorformidade',
            name='tempo_analise_causa_raiz',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 16, 6, 58, 37, 41506), null=True),
        ),
        migrations.AlterField(
            model_name='interacaoncorformidade',
            name='tempo_tratamento_definitivo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 16, 6, 58, 37, 41442), null=True),
        ),
        migrations.AlterField(
            model_name='interacaoncorformidade',
            name='tempo_tratamento_preliminar',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 16, 6, 58, 37, 41570), null=True),
        ),
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 19, 14, 58, 37, 32345), '1 Dia'), (datetime.datetime(2017, 7, 18, 18, 58, 37, 32345), '3 Dias'), (datetime.datetime(2017, 7, 17, 22, 58, 37, 32345), '5 Dias')]),
        ),
    ]
