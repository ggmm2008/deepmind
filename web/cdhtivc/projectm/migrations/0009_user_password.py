# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectm', '0008_auto_20160903_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='passWord',
            field=models.CharField(default='12345678x', max_length=20, verbose_name='\u5bc6\u7801'),
        ),
    ]
