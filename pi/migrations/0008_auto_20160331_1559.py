# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0007_auto_20160331_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outputfeature',
            old_name='actual_label',
            new_name='a_actual_label',
        ),
        migrations.RenameField(
            model_name='outputfeature',
            old_name='scored_label',
            new_name='a_scored_label',
        ),
        migrations.AddField(
            model_name='inputfeature',
            name='already_evaluated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='e_actual_label',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outputfeature',
            name='e_scored_label',
            field=models.FloatField(default=0.0),
        ),
    ]
