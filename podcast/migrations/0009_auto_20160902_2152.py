# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0008_auto_20160902_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='explicit',
            field=models.IntegerField(choices=[(1, 'yes'), (2, 'no'), (3, 'clean')], default=2),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='explicit',
            field=models.IntegerField(choices=[(1, 'yes'), (2, 'no'), (3, 'clean')], default=2),
        ),
    ]