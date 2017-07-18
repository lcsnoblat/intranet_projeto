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
            name='Chamado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField(verbose_name='Data da criação')),
                ('data_prevista_conclusao', models.DateTimeField(verbose_name='Data prevista de conclusão', null=True)),
                ('data_conclusao', models.DateTimeField(verbose_name='Data da conclusão', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('descricao', models.CharField(max_length=250)),
                ('chamado', models.ForeignKey(to='tihelp.Chamado')),
            ],
        ),
        migrations.CreateModel(
            name='TipoChamado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=255)),
                ('usuario_executante', models.ForeignKey(verbose_name='Usuário atendente', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TipoInteracao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=25)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TipoStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='interacao',
            name='tipo_interacao',
            field=models.ForeignKey(to='tihelp.TipoInteracao'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='status',
            field=models.ForeignKey(to='tihelp.TipoStatus'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='tipo',
            field=models.ForeignKey(to='tihelp.TipoChamado'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='usuario_solicitante',
            field=models.ForeignKey(verbose_name='Usuário solicitante', to=settings.AUTH_USER_MODEL),
        ),
    ]
