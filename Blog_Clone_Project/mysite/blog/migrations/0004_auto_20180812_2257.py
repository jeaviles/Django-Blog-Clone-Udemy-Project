# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-13 04:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180812_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 13, 4, 57, 25, 727348, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 13, 4, 57, 25, 726348, tzinfo=utc)),
        ),
    ]
