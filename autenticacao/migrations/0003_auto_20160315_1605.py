# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_auto_20160311_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='credentialsmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='CredentialsModel',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
