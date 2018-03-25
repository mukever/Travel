from datetime import datetime

from django.db import models

from spots.models import CityDict
# Create your models here.

class Hotel(models.Model):
    city = models.ForeignKey(CityDict,verbose_name="所属城市")
    address = models.CharField(max_length=150, verbose_name='酒店地址')
    name = models.CharField(max_length=52, verbose_name='酒店名字')
    desc =  models.CharField(max_length=300, verbose_name='酒店描述')
    detail = models.TextField(verbose_name='酒店详情')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name='难度')
    students = models.IntegerField(default=0, verbose_name='购买人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    category = models.CharField(default='高级', max_length=20, verbose_name='酒店类别')
    tag = models.CharField(default='', verbose_name='酒店标签', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name='入住须知')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '酒店'
        verbose_name_plural = verbose_name

    def get_rooms_nums(self):
        return self.room_set.all().count()

    def __str__(self):
        return self.name


class BannerHotel(Hotel):
    class Meta:
        verbose_name = u'轮播酒店'
        verbose_name_plural = verbose_name
        # 如果不设置 proxy ，就会再生成一个 BannerCourse 数据表
        proxy = True


# 房间信息
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='房间名称')
    desc = models.CharField(max_length=300, verbose_name='房间描述')
    price = models.IntegerField(default=0, verbose_name='房间价格')
    detail = models.TextField(verbose_name='房间详情')
    degree = models.CharField(choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), max_length=2, verbose_name='房型')
    nuy_nums = models.IntegerField(default=0, verbose_name='已经购买人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '房间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

