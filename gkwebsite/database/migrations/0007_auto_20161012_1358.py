# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-12 05:58
from __future__ import unicode_literals

import database.my_field
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20161007_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='area',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='^(\\d)+$')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='realName',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='volunteerList',
            field=database.my_field.ListField(blank=True, default=[]),
        ),
    ]
