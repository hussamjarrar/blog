# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-24 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 13, 51, 0, 178854, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 13, 51, 0, 176228, tzinfo=utc)),
        ),
    ]
