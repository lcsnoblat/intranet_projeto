# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-07 08:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0016_auto_20170705_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipochamadonconformidade',
            name='tempo_de_duracao',
            field=models.DateTimeField(choices=[(datetime.datetime(2017, 7, 8, 5, 28, 41, 64843), '1 Dia'), (datetime.datetime(2017, 7, 10, 5, 28, 41, 64843), '3 Dias'), (datetime.datetime(2017, 7, 12, 5, 28, 41, 64843), '5 Dias')], default=datetime.datetime(2017, 7, 7, 8, 28, 59, 565431, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
