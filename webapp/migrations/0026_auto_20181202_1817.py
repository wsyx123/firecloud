# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-02 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0025_auto_20181202_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=16)),
                ('passwd', models.CharField(blank=True, max_length=32, null=True)),
                ('last_password_change', models.CharField(blank=True, max_length=16, null=True)),
                ('password_expires', models.CharField(default='Never', max_length=16)),
                ('account_expires', models.CharField(default='Never', max_length=16)),
                ('status', models.IntegerField()),
                ('msg', models.CharField(blank=True, max_length=32, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.AssetHost')),
            ],
        ),
        migrations.RemoveField(
            model_name='hostuser',
            name='host',
        ),
        migrations.DeleteModel(
            name='HostUser',
        ),
    ]
