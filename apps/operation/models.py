from datetime import datetime

from django.db import models

# Create your models here.

from users.models import UserProfile
from schedules.models import Schedule
from hotels.models import Hotel
from spots.models import Spot,Ticket


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    schedule_name = models.CharField(max_length=50, verbose_name='行程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name





class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    # ID 是课程的 ID 或者是 讲师、课程机构的 ID
    fav_id = models.IntegerField(default=0, verbose_name='收藏数据 Id')
    fav_type = models.IntegerField(choices=( (1, '行程'), (2, '酒店'), (3, '景区') ), default=1, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    # 初始化判断是否收藏
    # has_fav = False
    # if request.user.is_authenticated():
    #     if UserProfile.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
    #         has_fav = True


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
    hotel = models.ForeignKey(Hotel, verbose_name='课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户入住过的酒店'
        verbose_name_plural = verbose_name

class UserSpot(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    spot = models.ForeignKey(Spot, verbose_name='景点')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户参观过的景点'
        verbose_name_plural = verbose_name


class UserSchedule(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    schedule = models.ForeignKey(Schedule, verbose_name='行程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户参观过的行程'
        verbose_name_plural = verbose_name


class ScheduleComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    schedule = models.ForeignKey(Schedule, verbose_name='行程')
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '行程评论'
        verbose_name_plural = verbose_name


class SpotComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    spot = models.ForeignKey(Spot, verbose_name='景点')
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '景点评论'
        verbose_name_plural = verbose_name

class HotelComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户')
    hotel = models.ForeignKey(Hotel, verbose_name='酒店')
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '酒店评论'
        verbose_name_plural = verbose_name