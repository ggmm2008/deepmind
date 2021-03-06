# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-28 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyCreateDate', models.DateField(default=None)),
                ('companyUpdateDate', models.DateTimeField(default=None)),
                ('companyName', models.CharField(max_length=200)),
                ('companyNature', models.CharField(choices=[('xxjs', '\u4fe1\u606f\u6280\u672f'), ('swzy', '\u751f\u7269\u5236\u836f')], default='yx', max_length=10)),
                ('companyAddress', models.CharField(max_length=500)),
                ('companyRegisteredDate', models.DateField(verbose_name='registered date')),
                ('registeredCaptital', models.FloatField()),
                ('legalRepresentative', models.CharField(max_length=10)),
                ('legalPhone', models.CharField(max_length=50)),
                ('companyAbstract', models.TextField()),
                ('industry', models.CharField(choices=[('xxjs', '\u4fe1\u606f\u6280\u672f'), ('swzy', '\u751f\u7269\u5236\u836f')], default='xxjs', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('industryName', models.CharField(max_length=20)),
                ('industryDescibe', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20)),
                ('userGroup', models.CharField(max_length=20)),
                ('department', models.CharField(choices=[('ts', '\u5929\u4f7f\u6295\u8d44\u90e8'), ('ct', '\u521b\u4e1a\u6295\u8d44\u90e8')], default='ts', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='companydata',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='projectm.User'),
        ),
    ]
