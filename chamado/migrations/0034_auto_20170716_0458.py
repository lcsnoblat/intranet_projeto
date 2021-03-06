# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-16 07:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0033_auto_20170716_0455'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamadonconformidade',
            name='validacao_gestor_atrasou',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 19, 12, 58, 7, 979439), '1 Dia'), (datetime.datetime(2017, 7, 18, 16, 58, 7, 979439), '3 Dias'), (datetime.datetime(2017, 7, 17, 20, 58, 7, 979439), '5 Dias')]),
        ),
    ]
