# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 20:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuApp', '0002_auto_20171030_2057'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuTest',
            new_name='Option',
        ),
    ]
