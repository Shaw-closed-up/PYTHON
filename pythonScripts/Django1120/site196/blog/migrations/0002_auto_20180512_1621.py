# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-12 16:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='保存日期'),
        ),
        migrations.AddField(
            model_name='post',
            name='mod_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2018, 5, 12, 16, 21, 20, 505880, tzinfo=utc), verbose_name='最后修改日期'),
            preserve_default=False,
        ),
    ]
