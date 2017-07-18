# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0010_auto_20160311_1638'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TipoStatus',
        ),
        migrations.RemoveField(
            model_name='interacao',
            name='tipo',
        ),
        migrations.DeleteModel(
            name='TipoInteracao',
        ),
    ]
