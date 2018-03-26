from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市')
    desc = models.TextField(verbose_name='城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Spot(models.Model):
    name = models.CharField(max_length=50, verbose_name='景区名称')
    category = models.CharField(max_length=20, choices=( ('1', '景区标签1'), ('2', '景区标签2'), ('3', '景区标签3') ),
                                default='1', verbose_name='景区类别' )
    desc = models.TextField(verbose_name='景区描述')
    detail = UEditorField(verbose_name='景区详情')
    tag = models.CharField(default=u'全国知名', max_length=10, verbose_name=u'景区标签')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    visit_nums = models.IntegerField(default=0, verbose_name='参观人数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    image = models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='封面图', max_length=100)
    address = models.CharField(max_length=150, verbose_name='景区地址')
    city = models.ForeignKey(CityDict, verbose_name='所在城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '景区信息'
        verbose_name_plural = verbose_name

    def get_tickets_nums(self):
        return self.ticket_set.all().count()


    def __str__(self):
        return self.name


class BannerSpot(Spot):
    class Meta:
        verbose_name = u'轮播景区'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True

class Ticket(models.Model):
    org = models.ForeignKey(Spot, verbose_name='所属景区')
    name = models.CharField(max_length=50, verbose_name='门票名字')
    price = models.IntegerField(default=0, verbose_name='价格')
    category = models.CharField(max_length=20, choices=(('1', '门票标签1'), ('2', '门票标签2'), ('3', '门票标签3')), default='1',
                                verbose_name='门票类别')
    desc = models.TextField(verbose_name='门票描述')
    detail = UEditorField(verbose_name='门票详情')
    tag = models.CharField(default=u'全国知名', max_length=10, verbose_name=u'门票标签')
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏数')
    buy_nums = models.IntegerField(default=0, verbose_name='购买人数')
    image = models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='封面图', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '门票'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
