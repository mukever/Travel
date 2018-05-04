from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.
from spots.models import CityDict


class Schedule(models.Model):
    name = models.CharField(max_length=52, verbose_name='行程名字')
    desc =  models.CharField(max_length=300, verbose_name='行程描述')
    detail = UEditorField(verbose_name='行程详情',blank=True)
    fav_nums = models.IntegerField(default=0, verbose_name='购买人数')
    price = models.IntegerField(default=0, verbose_name='价格')
    image = models.ImageField(upload_to='schedule/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    category = models.CharField(choices=(('1', '组团游'), ('2', '亲子游'), ('3', '自驾游')), max_length=2, verbose_name='旅游形式')
    tag = models.CharField(default='行程备注', verbose_name='行程备注', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name='行前须知')
    address = models.CharField(max_length=150, verbose_name='景区地址',blank=True)
    city = models.ForeignKey(CityDict, verbose_name='所在城市',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '行程'
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.name


class BannerSchedule(Schedule):
    class Meta:
        verbose_name = u'轮播行程'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True


class QinziSchedule(Schedule):
    class Meta:
        verbose_name = u'亲子游'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True


class ZutuanSchedule(Schedule):
    class Meta:
        verbose_name = u'组团游'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True