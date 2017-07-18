# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0008_chamadoanonimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='resolvido',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chamado',
            name='usuario_solicitante',
            field=models.ForeignKey(to='autenticacao.Usuario', verbose_name='Usuário solicitante'),
        ),
        migrations.AlterField(
            model_name='chamadoanonimo',
            name='presidente',
            field=models.ForeignKey(to='autenticacao.Usuario', verbose_name='presidente'),
        ),
        migrations.AlterField(
            model_name='interacao',
            name='usuario',
            field=models.ForeignKey(to='autenticacao.Usuario', verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='tipochamado',
            name='usuario_executante',
            field=models.ForeignKey(to='autenticacao.Usuario', verbose_name='Usuário atendente'),
        ),
    ]
