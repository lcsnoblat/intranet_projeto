# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuais', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manual',
            name='tipo',
            field=models.ForeignKey(to='manuais.TipoManual', default=1),
            preserve_default=False,
        ),
    ]
