# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectm', '0005_auto_20160830_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydata',
            name='companyId',
            field=models.CharField(default=None, max_length=8, verbose_name='\u9879\u76ee\u7f16\u53f7'),
        ),
    ]
