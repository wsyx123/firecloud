# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-23 18:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181217_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scriptmodel',
            old_name='script_owner',
            new_name='owner',
        ),
    ]