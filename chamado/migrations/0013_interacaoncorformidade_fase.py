# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-04 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0012_auto_20170704_0223'),
    ]

    operations = [
        migrations.AddField(
            model_name='interacaoncorformidade',
            name='fase',
            field=models.CharField(choices=[('INICIAL', 'INICIAL'), ('INTERMEDIARIO', 'INTERMEDIARIO'), ('FINAL', 'FINAL')], default='INICIAL', max_length=50),
        ),
    ]
