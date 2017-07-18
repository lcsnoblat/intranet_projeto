# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0002_chamado_ativar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='ativar',
            field=models.BooleanField(verbose_name='Enviar Email e ativar chamado', default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chamado',
            name='descricao',
            field=models.CharField(verbose_name='Faça uma breve descrição do chamado', max_length=750),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo de chamado', to='tihelp.TipoChamado'),
        ),
    ]
