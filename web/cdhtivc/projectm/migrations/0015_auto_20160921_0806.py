# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectm', '0014_auto_20160915_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydata',
            name='companyFollowSuggest',
            field=models.CharField(choices=[('\u4e00\u822c\u5173\u6ce8', '\u4e00\u822c\u5173\u6ce8'), ('\u91cd\u70b9\u5173\u6ce8', '\u91cd\u70b9\u5173\u6ce8'), ('\u6682\u7f13\u9879\u76ee', '\u6682\u7f13\u9879\u76ee'), ('\u7acb\u9879', '\u7acb\u9879'), ('\u5df2\u8fc7\u4f1a', '\u5df2\u8fc7\u4f1a'), ('\u5df2\u62e8\u6b3e', '\u5df2\u62e8\u6b3e')], default='ybgz', max_length=10, verbose_name='\u8ddf\u8fdb\u5efa\u8bae'),
        ),
        migrations.AlterField(
            model_name='companydata',
            name='industry',
            field=models.CharField(choices=[('\u65b0\u4e00\u4ee3\u4fe1\u606f\u6280\u672f', '\u65b0\u4e00\u4ee3\u4fe1\u606f\u6280\u672f'), ('\u751f\u7269\u5236\u836f', '\u751f\u7269\u5236\u836f'), ('\u8282\u80fd\u73af\u4fdd', '\u8282\u80fd\u73af\u4fdd'), ('\u9ad8\u7aef\u88c5\u5907\u5236\u9020', '\u9ad8\u7aef\u88c5\u5907\u5236\u9020')], default='xxjs', max_length=10, verbose_name='\u884c\u4e1a\u7c7b\u578b'),
        ),
    ]