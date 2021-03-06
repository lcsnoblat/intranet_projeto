# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-05 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0015_auto_20170705_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamadonconformidade',
            name='descricao_causa_raiz',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamadonconformidade',
            name='descricao_tratamento_definitivo',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chamadonconformidade',
            name='descricao_tratamento_preliminar',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chamadonconformidade',
            name='arquivo',
            field=models.FileField(max_length=300, upload_to=''),
        ),
    ]
