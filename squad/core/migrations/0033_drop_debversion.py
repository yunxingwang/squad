# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_testrun_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='version',
            field=models.CharField(max_length=100),
        ),
    ]