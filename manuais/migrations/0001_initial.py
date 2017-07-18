# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
                ('arquivo', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('usuario_criador', models.ForeignKey(verbose_name='Usuário que realizou o upload', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoManual',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
    ]
