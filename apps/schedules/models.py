from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.db import models

# Create your models here.


class Schedule(models.Model):
    name = models.CharField(max_length=52, verbose_name='行程名字')
    desc =  models.CharField(max_length=300, verbose_name='行程描述')
    detail = UEditorField(verbose_name='行程详情')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name='难度')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    buy_nums= models.IntegerField(default=0, verbose_name='购买人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    category = models.CharField(default='后端', max_length=20, verbose_name='行程类别')
    tag = models.CharField(default='', verbose_name='行程标签', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name='行前须知')
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


