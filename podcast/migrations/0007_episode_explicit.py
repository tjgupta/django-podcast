# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0006_podcast_explicit'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='explicit',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('clean', 'clean')], default='yes', max_length=5),
            preserve_default=False,
        ),
    ]
