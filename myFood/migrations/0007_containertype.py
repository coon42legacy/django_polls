# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFood', '0006_auto_20160425_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
