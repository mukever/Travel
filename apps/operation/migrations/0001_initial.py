# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-14 05:16
from __future__ import unicode_literals

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
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='收藏数据 Id')),
                ('fav_type', models.IntegerField(choices=[(1, '行程'), (2, '酒店房间'), (3, '景区门票')], default=1, verbose_name='购买类型')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户购买',
                'verbose_name_plural': '用户购买',
            },
        ),
        migrations.CreateModel(
            name='UserHotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户预定过的酒店',
                'verbose_name_plural': '用户预定过的酒店',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接受用户')),
                ('message', models.CharField(max_length=500, verbose_name='消息内容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='UserSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户参观过的行程',
                'verbose_name_plural': '用户参观过的行程',
            },
        ),
        migrations.CreateModel(
            name='UserSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('spot', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='spots.Ticket', verbose_name='景点门票')),
            ],
            options={
                'verbose_name': '用户购买过的门票',
                'verbose_name_plural': '用户购买过的门票',
            },
        ),
    ]