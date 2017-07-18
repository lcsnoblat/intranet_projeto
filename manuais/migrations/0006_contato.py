# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import manuais.models


class Migration(migrations.Migration):

    dependencies = [
        ('manuais', '0005_tipomanual_material_comercial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
                #('arquivo', models.FileField(upload_to=manuais.models.Contato.path_arquivo)),
            ],
        ),
    ]
