# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0034_auto_20161101_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timer',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=50),
        ),
    ]
