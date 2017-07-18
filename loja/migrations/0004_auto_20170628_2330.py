# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-29 02:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20170328_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('SOLICITADO', 'Pedido solicitado'), ('RECUSADO', 'Pedido recusado'), ('ACEITO', 'Pedido aceito'), ('ENVIADO', 'Pedido enviado'), ('DISPONIVEL', 'Pedido disponível')], default='SOLICITADO', max_length=25),
        ),
    ]
