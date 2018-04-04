# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-04 13:53
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='酒店地址')),
                ('name', models.CharField(max_length=52, verbose_name='酒店名字')),
                ('desc', models.CharField(max_length=300, verbose_name='酒店描述')),
                ('detail', DjangoUeditor.models.UEditorField(blank=True, verbose_name='酒店详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度')),
                ('buy_nums', models.IntegerField(default=0, verbose_name='购买人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='hotel/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否是轮播图')),
                ('category', models.CharField(default='高级', max_length=20, verbose_name='酒店类别')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='酒店标签')),
                ('youneed_konw', models.CharField(default='', max_length=300, verbose_name='入住须知')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spots.CityDict', verbose_name='所属城市')),
            ],
            options={
                'verbose_name': '酒店',
                'verbose_name_plural': '酒店',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='房间名称')),
                ('desc', models.CharField(max_length=300, verbose_name='房间描述')),
                ('price', models.IntegerField(default=0, verbose_name='房间价格')),
                ('detail', DjangoUeditor.models.UEditorField(verbose_name='房间详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='房型')),
                ('nuy_nums', models.IntegerField(default=0, verbose_name='已经购买人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='hotelroom/%Y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel', verbose_name='所属酒店')),
            ],
            options={
                'verbose_name': '房间',
                'verbose_name_plural': '房间',
            },
        ),
        migrations.CreateModel(
            name='BannerHotel',
            fields=[
            ],
            options={
                'verbose_name': '轮播酒店',
                'verbose_name_plural': '轮播酒店',
                'proxy': True,
            },
            bases=('hotels.hotel',),
        ),
    ]
