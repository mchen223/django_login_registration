# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0002_auto_20170727_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
