# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_auto_20180920_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('phone', models.IntegerField(max_length=32)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
