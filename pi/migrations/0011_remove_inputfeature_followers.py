# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0010_auto_20160331_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputfeature',
            name='Followers',
        ),
    ]
