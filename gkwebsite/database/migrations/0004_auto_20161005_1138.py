# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-05 03:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_auto_20161004_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='account',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(regex='(\\d|\\w){4,}$')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(default='', max_length=50, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='12345678', max_length=50, validators=[django.core.validators.RegexValidator(regex='(\\d|\\w){4,}$')]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator(regex='(\\d)+$')]),
        ),
    ]