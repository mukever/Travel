__author__ = 'zaxlct'
__date__ = '2017/4/2 下午5:40'

from .models import UserFavorite, UserMessage
from .models import UserHotel,UserSpot,UserSchedule

import xadmin


# 用户收藏
class UserFavoriteAdmin:
    list_display = ['user', 'data_tag', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']




# 用户消息
class UserMessageAdmin:
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    # 这里的 user 不是 ForeignKey ，具体请看 models.py
    list_filter = ['user', 'message', 'has_read', 'add_time']



class UserHotelAdmin:
    list_display = ['user', 'hotel','add_time']
    search_fields = ['user', 'hotel',]
    list_filter = ['user', 'hotel', 'add_time']


class UserSpotAdmin:
    list_display = ['user', 'spot', 'add_time']
    search_fields = ['user', 'spot']
    list_filter = ['user', 'add_time']


class UserScheduleAdmin:
    list_display = ['user', 'schedule', 'add_time']
    search_fields = ['user', 'schedule']
    list_filter = ['user', 'schedule', 'add_time']


xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)


xadmin.site.register(UserSchedule, UserScheduleAdmin)
xadmin.site.register(UserSpot, UserSpotAdmin)
xadmin.site.register(UserHotel, UserHotelAdmin)