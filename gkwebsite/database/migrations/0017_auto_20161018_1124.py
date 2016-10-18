# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-18 03:24
from __future__ import unicode_literals

import database.my_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='groupList',
            field=database.my_field.ListField(blank=True, default=[]),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='groupList',
            field=database.my_field.ListField(blank=True, default=[]),
        ),
    ]
