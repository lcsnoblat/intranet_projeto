# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-16 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0034_auto_20170716_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 19, 13, 24, 18, 326542), '1 Dia'), (datetime.datetime(2017, 7, 18, 17, 24, 18, 326542), '3 Dias'), (datetime.datetime(2017, 7, 17, 21, 24, 18, 326542), '5 Dias')]),
        ),
    ]
