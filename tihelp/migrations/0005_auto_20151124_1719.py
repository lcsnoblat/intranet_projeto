# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0004_auto_20151119_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='interacao',
            name='data_interacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 17, 19, 10, 827287), verbose_name='Data da interacao'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interacao',
            name='descricao',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='interacao',
            name='tipo_interacao',
            field=models.ForeignKey(verbose_name='Tipo da Interação', to='tihelp.TipoInteracao'),
        ),
    ]
