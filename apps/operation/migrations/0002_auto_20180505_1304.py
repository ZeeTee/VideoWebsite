# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-05 13:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavorite',
            name='video',
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u6dfb\u52a0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(default=0, verbose_name='\u6570\u636eid'),
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf\u7c7b\u578b'),
        ),
    ]