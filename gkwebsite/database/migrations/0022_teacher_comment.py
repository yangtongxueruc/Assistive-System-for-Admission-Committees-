# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-20 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0021_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
    ]
