# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-12 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolvido', models.BooleanField()),
                ('data_criacao', models.DateTimeField(verbose_name='Data da criação')),
                ('data_conclusao', models.DateTimeField(blank=True, null=True, verbose_name='Data da conclusão')),
            ],
        ),
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=750, verbose_name='Faça uma interacao')),
            ],
        ),
        migrations.CreateModel(
            name='TipoChamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ChamadoDP',
            fields=[
                ('chamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Chamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=750, verbose_name='Faça uma descrição do chamado')),
            ],
            bases=('chamado.chamado',),
        ),
        migrations.CreateModel(
            name='ChamadoMKT',
            fields=[
                ('chamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Chamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('foco', models.CharField(max_length=750, verbose_name='Diga qual o foco')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('telefone', models.CharField(max_length=11)),
                ('tamanho', models.CharField(max_length=15)),
                ('data_prevista', models.DateTimeField(blank=True, null=True, verbose_name='Data prevista de conclusão')),
                ('formato', models.CharField(max_length=10)),
            ],
            bases=('chamado.chamado',),
        ),
        migrations.CreateModel(
            name='ChamadoTI',
            fields=[
                ('chamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Chamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=750, verbose_name='Faça uma descrição do chamado')),
            ],
            bases=('chamado.chamado',),
        ),
        migrations.CreateModel(
            name='InteracaoDP',
            fields=[
                ('interacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Interacao')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chamado_interacao_DP_chamado', to='chamado.ChamadoDP')),
            ],
            bases=('chamado.interacao',),
        ),
        migrations.CreateModel(
            name='InteracaoMKT',
            fields=[
                ('interacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Interacao')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chamado_interacao_MKT_chamado', to='chamado.ChamadoMKT')),
            ],
            bases=('chamado.interacao',),
        ),
        migrations.CreateModel(
            name='InteracaoTI',
            fields=[
                ('interacao_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.Interacao')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('chamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chamado_interacao_ti_chamado', to='chamado.ChamadoTI')),
            ],
            bases=('chamado.interacao',),
        ),
        migrations.CreateModel(
            name='TipoChamadoDP',
            fields=[
                ('tipochamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.TipoChamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('chamado.tipochamado',),
        ),
        migrations.CreateModel(
            name='TipoChamadoMKT',
            fields=[
                ('tipochamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.TipoChamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('chamado.tipochamado',),
        ),
        migrations.CreateModel(
            name='TipoChamadoTI',
            fields=[
                ('tipochamado_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='chamado.TipoChamado')),
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
            ],
            bases=('chamado.tipochamado',),
        ),
        migrations.AddField(
            model_name='tipochamado',
            name='usuario_executante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_tipo_chamado_chamado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interacao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interacao_chamado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chamado',
            name='usuario_solicitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_chamado_chamado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chamadoti',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamado.TipoChamadoTI', verbose_name='tipo'),
        ),
        migrations.AddField(
            model_name='chamadomkt',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamado.TipoChamadoMKT', verbose_name='tipo'),
        ),
        migrations.AddField(
            model_name='chamadodp',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamado.TipoChamadoDP', verbose_name='tipo'),
        ),
    ]