# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0011_auto_20160311_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chamado',
            name='ativar',
        ),
    ]
