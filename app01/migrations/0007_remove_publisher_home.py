# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20180920_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='home',
        ),
    ]
