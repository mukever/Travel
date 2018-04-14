__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import HotelDetailView, HotelHomeView, AddFavView, HotelDescView, \
    HotelListView, HotelRoomView, RoomDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', HotelListView.as_view(), name='hotels_list'),
    # url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),

    url(r'^home/(?P<hotel_id>\d+)/$', HotelHomeView.as_view(), name='hotel_home'),
    url(r'^detail/(?P<hotel_id>\d+)/$', HotelDetailView.as_view(), name='hotel_detail'),
    url(r'^desc/(?P<hotel_id>\d+)/$', HotelDescView.as_view(), name='hotel_desc'),
    url(r'^room/(?P<hotel_id>\d+)/$', HotelRoomView.as_view(), name='hotel_room'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),

    # room详情页
    url(r'^room/detail/(?P<room_id>\d+)/$', RoomDetailView.as_view(), name='room_detail'),

]
