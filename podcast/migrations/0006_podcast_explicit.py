# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0005_auto_20160830_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='explicit',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no'), ('clean', 'clean')], default='no', max_length=5),
            preserve_default=False,
        ),
    ]
