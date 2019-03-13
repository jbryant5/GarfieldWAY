# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-13 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import pins.models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0004_auto_20190123_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='other_pin_room',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name=b'pin_room',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[pins.models.validate_room]),
        ),
    ]
