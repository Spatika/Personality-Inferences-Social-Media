# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0005_auto_20160330_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputfeature',
            name='photos_uploaded',
            field=models.IntegerField(default=0),
        ),
    ]
