# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tihelp', '0003_auto_20151119_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='interacao',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1, verbose_name='Usuário'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chamado',
            name='descricao',
            field=models.CharField(max_length=750, verbose_name='Faça uma descrição do chamado'),
        ),
    ]
