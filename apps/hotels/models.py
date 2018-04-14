from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

from spots.models import CityDict
# Create your models here.

class Hotel(models.Model):
    city = models.ForeignKey(CityDict,verbose_name="所属城市")
    address = models.CharField(max_length=150, verbose_name='酒店地址')
    name = models.CharField(max_length=52, verbose_name='酒店名字')
    desc =  models.CharField(max_length=300, verbose_name='酒店描述')
    detail = UEditorField(verbose_name='酒店详情',  upload_settings={"imageMaxSize":1204000},
             settings={},command=None,blank=True)
    category = models.CharField(choices=(('1', '经济型'), ('2', '舒适型'), ('3', '高档型')), max_length=2, verbose_name='酒店级别')
    fav_nums = models.IntegerField(default=0, verbose_name='购买人数')
    image = models.ImageField(upload_to='hotel/%Y/%m', verbose_name='封面图', max_length=100,blank=True)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    is_banner = models.BooleanField(default=False, verbose_name=u'是否是轮播图')
    tag = models.CharField(default='热门销售', verbose_name='酒店标签', max_length=10)
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
    hotel = models.ForeignKey(Hotel, verbose_name='所属酒店')
    name = models.CharField(max_length=100, verbose_name='房间名称')
    desc = models.CharField(max_length=300, verbose_name='房间描述')
    price = models.IntegerField(default=0, verbose_name='房间价格')
    detail = UEditorField(verbose_name='房间详情')
    degree = models.CharField(choices=(('1','标准'),('2', '双人间'), ('3', '情侣'), ('4', '家庭房'),), max_length=2, verbose_name='房型')
    fav_nums = models.IntegerField(default=0, verbose_name='已购买人数人数')
    image = models.ImageField(upload_to='hotelroom/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '房间'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

