# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-02 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0011_remove_inputfeature_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputfeature',
            name='Analytic',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='inputfeature',
            name='Authentic',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='inputfeature',
            name='Clout',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='inputfeature',
            name='Tone',
            field=models.FloatField(default=0.0),
        ),
    ]
