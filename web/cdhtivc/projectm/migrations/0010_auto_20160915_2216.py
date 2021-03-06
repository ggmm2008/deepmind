# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-15 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectm', '0009_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='companyFinancialNeeds',
            field=models.TextField(blank=True, default=None, verbose_name='\u516c\u53f8\u878d\u8d44\u9700\u6c42'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyFinancialSituation',
            field=models.TextField(blank=True, default=None, verbose_name='\u516c\u53f8\u8d22\u52a1\u6307\u6807'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyName',
            field=models.CharField(error_messages={'required': '\u540d\u79f0\u4e0d\u80fd\u672a\u7a7a'}, max_length=200, verbose_name='\u516c\u53f8\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyProjectPassDate',
            field=models.DateField(blank=True, default=None, verbose_name='\u8fc7\u4f1a\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyProjectSetUpTime',
            field=models.DateField(blank=True, default=None, verbose_name='\u7acb\u9879\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyRemarks',
            field=models.TextField(blank=True, default=None, verbose_name='\u516c\u53f8\u5176\u4ed6\u5907\u6ce8\u60c5\u51b5'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='companyUpdateDate',
            field=models.DateTimeField(blank=True, default=None, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
