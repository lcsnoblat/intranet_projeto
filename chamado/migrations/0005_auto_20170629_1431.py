# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-29 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0004_auto_20170628_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamadonconformidade',
            name='document',
            field=models.FileField(default='', upload_to='/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.Produto', verbose_name='produto'),
        ),
    ]
