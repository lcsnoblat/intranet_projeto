# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tihelp', '0005_auto_20151124_1719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interacao',
            old_name='tipo_interacao',
            new_name='tipo',
        ),
    ]
