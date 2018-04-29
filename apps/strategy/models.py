from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

from spots.models import CityDict
# Create your models here.

class Strategy(models.Model):
    city = models.ForeignKey(CityDict,verbose_name="所属城市")
    name = models.CharField(max_length=52, verbose_name='攻略名字')
    desc =  models.CharField(max_length=300, verbose_name='攻略描述')
    detail = UEditorField(verbose_name='攻略详情',  upload_settings={"imageMaxSize":1204000},
             settings={},command=None,blank=True)
    category = models.CharField(choices=(('1', '经济型'), ('2', '畅玩型'), ('3', '高档型')), max_length=2, verbose_name='攻略级别')
    fav_nums = models.IntegerField(default=0, verbose_name='购买人数')
    image = models.ImageField(upload_to='hotel/%Y/%m', verbose_name='封面图', max_length=100,blank=True)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    tag = models.CharField(default='热门销售', verbose_name='攻略标签', max_length=10)
    youneed_konw = models.CharField(default='', max_length=300, verbose_name='购买须知')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '攻略'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
