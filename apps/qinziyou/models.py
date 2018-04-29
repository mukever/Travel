from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.
from spots.models import CityDict


class Qinziyou(models.Model):
    name = models.CharField(max_length=52, verbose_name='亲子游名字')
    desc =  models.CharField(max_length=300, verbose_name='亲子游描述')
    detail = UEditorField(verbose_name='亲子游详情',blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name='购买人数')
    price = models.IntegerField(default=0, verbose_name='价格')
    image = models.ImageField(upload_to='schedule/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    tag = models.CharField(default='亲子游备注', verbose_name='亲子游备注', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name='行前须知')
    address = models.CharField(max_length=150, verbose_name='亲子游前往地址',blank=True)
    city = models.ForeignKey(CityDict, verbose_name='所在城市',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '亲子游'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name



