# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-16 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0051_auto_20161110_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admissionStatus',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
