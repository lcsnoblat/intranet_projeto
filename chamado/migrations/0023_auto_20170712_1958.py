# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-12 22:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0022_auto_20170712_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 12, 20, 58, 50, 878686), '1 Dia'), (datetime.datetime(2017, 7, 15, 19, 58, 50, 878686), '3 Dias'), (datetime.datetime(2017, 7, 17, 19, 58, 50, 878686), '5 Dias')]),
        ),
    ]