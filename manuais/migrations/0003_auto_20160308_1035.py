# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuais', '0002_manual_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manual',
            name='tipo',
            field=models.ForeignKey(verbose_name='Tipo de manual', to='manuais.TipoManual'),
        ),
    ]
