from datetime import datetime

from django.db import models

# Create your models here.
from qinziyou.models import Qinziyou
from users.models import UserProfile
from schedules.models import Schedule
from hotels.models import Hotel, Room
from spots.models import Spot,Ticket
from zutuanyou.models import Zutuanyou


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    fav_id = models.IntegerField(default=0, verbose_name='收藏数据 Id')
    fav_type = models.IntegerField(choices=( (1, '行程'), (2, '酒店房间'), (3, '景区门票'), (4, '组团游') , (5, '亲子游')   ), default=1, verbose_name='购买类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户购买'
        verbose_name_plural = verbose_name

    def data_tag(self):
        if self.fav_type == 1:
            return Schedule.objects.filter(id=self.fav_id).first()
        elif self.fav_type ==2:
            return Room.objects.filter(id=self.fav_id).first()
        elif self.fav_type == 3:
            return Ticket.objects.filter(id=self.fav_id).first()
        elif self.fav_type == 4:
            return Zutuanyou.objects.filter(id=self.fav_id).first()
        elif self.fav_type == 5:
            return Qinziyou.objects.filter(id=self.fav_id).first()

    data_tag.short_description = '购买物品'
    data_tag.allow_tags = True


class UserMessage(models.Model):
    # 如果 为 0 代表全局消息，否则就是用户的 ID

    user = models.IntegerField(default=0, verbose_name='接受用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name



class UserHotel(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    hotel = models.ForeignKey(Room, verbose_name='酒店房间',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户预定过的酒店'
        verbose_name_plural = verbose_name

class UserSpot(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    spot = models.ForeignKey(Ticket, verbose_name='景点门票',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户购买过的门票'
        verbose_name_plural = verbose_name

    # def spot(self):
    #     return Spot.objects.filter(id=self.ticket.id).first()

class UserSchedule(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    schedule = models.ForeignKey(Schedule, verbose_name='行程',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户参观过的行程'
        verbose_name_plural = verbose_name


class UserQinziyou(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    qinziyou = models.ForeignKey(Qinziyou, verbose_name='亲子游',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户参加的亲子游'
        verbose_name_plural = verbose_name

class UserZutuanyou(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    zutuanyou = models.ForeignKey(Zutuanyou, verbose_name='组团游',blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户参加的组团游'
        verbose_name_plural = verbose_name
