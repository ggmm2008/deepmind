# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-15 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectm', '0011_auto_20160915_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='companyProjectPassDate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='\u8fc7\u4f1a\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyProjectSetUpTime',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='\u7acb\u9879\u65e5\u671f'),
        ),
    ]
