# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-19 12:25
from __future__ import unicode_literals

import database.my_field
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_picture_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='major',
            field=database.my_field.ListField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='major',
            field=database.my_field.ListField(blank=True, default=[]),
        ),
    ]
