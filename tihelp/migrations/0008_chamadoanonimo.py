# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tihelp', '0007_auto_20151124_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChamadoAnonimo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=750, verbose_name='Faça uma descrição do chamado')),
                ('data_criacao', models.DateTimeField(verbose_name='Data da criação')),
                ('presidente', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='presidente')),
            ],
        ),
    ]
