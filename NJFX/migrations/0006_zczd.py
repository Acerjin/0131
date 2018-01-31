# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NJFX', '0005_auto_20180126_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zczd',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('srlb', models.CharField(choices=[('债券逆回购', '债券逆回购'), ('其他货币类', '其他货币类'), ('协议存款', '协议存款'), ('国债', '国债'), ('企业债', '企业债'), ('可转债', '可转债'), ('另类产品', '另类产品'), ('其他固定类', '其他固定类'), ('股票', '股票'), ('其他权益类', '其他权益类'), ('备用', '备用')], max_length=15, verbose_name='收入类别')),
                ('tzlb', models.CharField(choices=[('银行存款', '银行存款'), ('债券逆回购', '债券逆回购'), ('央行票据', '央行票据'), ('货币基金', '货币基金'), ('协议/定期存款/国债', '协议/定期存款/国债'), ('23/24号文产品', '23/24号文产品'), ('企业债', '企业债'), ('其它固定类', '其它固定类'), ('其它货币基金', '其它货币基金'), ('股票', '股票'), ('股票基金', '股票基金'), ('比例', '比例'), ('备用', '备用')], max_length=15, verbose_name='投资类别')),
                ('zcmc', models.CharField(max_length=50, verbose_name='资产名称')),
            ],
            options={
                'verbose_name': '资产分类关系',
                'verbose_name_plural': '资产分类关系',
            },
        ),
    ]
