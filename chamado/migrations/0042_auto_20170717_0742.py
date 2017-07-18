# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-17 10:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0041_auto_20170717_0310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_causa_raiz',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 42, 42, 52194, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_analise_procecencia',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 42, 42, 52051, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_definitivo',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 42, 42, 52113, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='tempo_tratamento_preliminar',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 7, 17, 10, 42, 42, 52249, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 20, 15, 42, 42, 49612), '1 Dia'), (datetime.datetime(2017, 7, 19, 19, 42, 42, 49612), '3 Dias'), (datetime.datetime(2017, 7, 18, 23, 42, 42, 49612), '5 Dias')]),
        ),
    ]