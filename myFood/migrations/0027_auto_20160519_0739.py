# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-19 07:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0026_auto_20160509_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
