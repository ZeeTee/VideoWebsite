# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-06 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20180505_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='videores',
            name='times',
            field=models.IntegerField(default=0, verbose_name='\u65f6\u957f'),
        ),
    ]