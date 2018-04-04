__author__ = 'zaxlct'
__date__ = '2017/4/2 下午5:40'

from .models import UserAsk, UserFavorite, UserMessage
from .models import UserHotel,UserSpot,UserSchedule
from .models import ScheduleComments,SpotComments,HotelComments
import xadmin

#用户留言
class UserAskAdmin:
    list_display = ['name', 'mobile', 'schedule_name', 'add_time']
    search_fields = ['name', 'mobile', 'schedule_name']
    list_filter = ['name', 'mobile', 'schedule_name', 'add_time']

# 用户收藏
class UserFavoriteAdmin:
    list_display = ['user_id__email', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user_id__email', 'fav_id', 'fav_type']
    list_filter = ['user_id__email', 'fav_id', 'fav_type', 'add_time']

# 用户消息
class UserMessageAdmin:
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    # 这里的 user 不是 ForeignKey ，具体请看 models.py
    list_filter = ['user', 'message', 'has_read', 'add_time']





class HotelCommentsAdmin:
    list_display = ['user', 'hotel', 'comments', 'add_time']
    search_fields = ['user', 'hotel', 'comments']
    list_filter = ['user__nick_name', 'hotel__name', 'comments', 'add_time']

class SpotCommentsAdmin:
    list_display = ['user', 'spot', 'comments', 'add_time']
    search_fields = ['user', 'spot', 'comments']
    list_filter = ['user__nick_name', 'spot__name', 'comments', 'add_time']

class ScheduleCommentsAdmin:
    list_display = ['user', 'schedule', 'comments', 'add_time']
    search_fields = ['user', 'schedule', 'comments']
    list_filter = ['user__nick_name', 'schedule__name', 'comments', 'add_time']



class UserHotelAdmin:
    list_display = ['user', 'hotel', 'add_time']
    search_fields = ['user', 'hotel']
    list_filter = ['user__nick_name', 'hotel__name', 'add_time']


class UserSpotAdmin:
    list_display = ['user', 'spot', 'add_time']
    search_fields = ['user', 'spot']
    list_filter = ['user__nick_name', 'spot__name', 'add_time']


class UserScheduleAdmin:
    list_display = ['user', 'schedule', 'add_time']
    search_fields = ['user', 'schedule']
    list_filter = ['user__nick_name', 'schedule__name', 'add_time']







xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)

xadmin.site.register(ScheduleComments, ScheduleCommentsAdmin)
xadmin.site.register(SpotComments, SpotCommentsAdmin)
xadmin.site.register(HotelComments, HotelCommentsAdmin)

xadmin.site.register(UserSchedule, UserScheduleAdmin)
xadmin.site.register(UserSpot, UserSpotAdmin)
xadmin.site.register(UserHotel, UserHotelAdmin)