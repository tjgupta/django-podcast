# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 23:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0004_auto_20160830_2308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='episode',
        ),
        migrations.RemoveField(
            model_name='video',
            name='episode',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]