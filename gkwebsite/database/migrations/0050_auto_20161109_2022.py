# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-09 12:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0049_auto_20161109_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='send_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
