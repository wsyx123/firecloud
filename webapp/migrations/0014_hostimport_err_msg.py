# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-19 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20181116_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostimport',
            name='err_msg',
            field=models.TextField(blank=True, null=True, verbose_name='\u9519\u8bef\u4fe1\u606f'),
        ),
    ]
