# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0015_remove_meal_container_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='container_types',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myFood.ContainerType'),
            preserve_default=False,
        ),
    ]