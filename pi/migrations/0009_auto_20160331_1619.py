# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 08:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0008_auto_20160331_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='outputfeature',
            name='c_actual_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='c_scored_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='es_actual_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='es_scored_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='o_actual_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='o_scored_label',
            field=models.FloatField(default=0.0),
        ),
    ]
