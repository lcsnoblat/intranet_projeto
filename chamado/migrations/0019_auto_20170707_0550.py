# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-07 08:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0018_auto_20170707_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 8, 5, 50, 19, 364917), '1 Dia'), (datetime.datetime(2017, 7, 10, 5, 50, 19, 364917), '3 Dias'), (datetime.datetime(2017, 7, 12, 5, 50, 19, 364917), '5 Dias')]),
        ),
    ]
