# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-05 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_auto_20180505_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfavorite',
            name='fav_type',
        ),
        migrations.AddField(
            model_name='userfavorite',
            name='is_fav',
            field=models.IntegerField(default=0, verbose_name='\u6536\u85cf'),
        ),
    ]
