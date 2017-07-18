# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuais', '0004_auto_20160308_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipomanual',
            name='material_comercial',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
