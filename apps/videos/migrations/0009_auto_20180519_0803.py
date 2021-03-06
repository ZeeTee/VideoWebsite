# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-19 08:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20180515_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='', max_length=200, verbose_name='\u8bbf\u95ee\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video', verbose_name='\u6240\u5c5e\u89c6\u9891'),
        ),
        migrations.AlterField(
            model_name='videores',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Lesson', verbose_name='\u6240\u5c5e\u5206\u96c6'),
        ),
    ]
