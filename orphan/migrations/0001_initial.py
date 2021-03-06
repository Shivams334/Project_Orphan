# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project_progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=60)),
                ('project_discription', models.TextField()),
                ('project_stack', models.CharField(max_length=100)),
                ('project_link', models.URLField()),
                ('owner_name', models.CharField(max_length=50)),
                ('Project_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orphan.Project_progress')),
            ],
        ),
    ]
