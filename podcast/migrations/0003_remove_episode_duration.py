# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0002_auto_20160830_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='duration',
        ),
    ]
