# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-05-15 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20180515_1120'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailVeryfyRecord',
            new_name='EmailVerifyRecord',
        ),
    ]