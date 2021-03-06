# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 22:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('filename', models.CharField(max_length=255)),
                ('mime', models.CharField(max_length=40)),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcast.Episode')),
            ],
        ),
    ]
