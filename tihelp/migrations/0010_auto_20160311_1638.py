# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0009_auto_20160311_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamado',
            name='status',
        ),
        migrations.RemoveField(
            model_name='chamadoanonimo',
            name='presidente',
        ),
        migrations.AlterField(
            model_name='chamado',
            name='usuario_solicitante',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário solicitante'),
        ),
        migrations.AlterField(
            model_name='interacao',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='tipochamado',
            name='usuario_executante',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário atendente'),
        ),
    ]
