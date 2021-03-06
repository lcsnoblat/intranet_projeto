# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0042_auto_20170717_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_causa_raiz',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 43, 18, 964893, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_procecencia',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 43, 18, 964748, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_definitivo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 43, 18, 964810, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_preliminar',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 43, 18, 964948, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 20, 15, 43, 18, 962321), '1 Dia'), (datetime.datetime(2017, 7, 19, 19, 43, 18, 962321), '3 Dias'), (datetime.datetime(2017, 7, 18, 23, 43, 18, 962321), '5 Dias')]),
        ),
    ]
