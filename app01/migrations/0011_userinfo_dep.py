# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Department'),
        ),
    ]
