# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_itunesmetadata_podcast'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='podcast',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='podcast.Podcast'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='itunesmetadata',
            name='podcast',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='podcast.Podcast'),
            preserve_default=False,
        ),
    ]