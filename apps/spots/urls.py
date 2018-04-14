__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import *
urlpatterns = [
    # 课程列表页
    url(r'^list/$', SpotListView.as_view(), name='spots_list'),
    url(r'^detail/(?P<spot_id>\d+)/$', SpotDetailView.as_view(), name='spot_detail'),

    # url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),

    url(r'^home/(?P<spot_id>\d+)/$', SpotHomeView.as_view(), name='spot_home'),
    url(r'^desc/(?P<spot_id>\d+)/$', SpotDescView.as_view(), name='spot_desc'),
    url(r'^ticket/(?P<spot_id>\d+)/$', SpotTicketView.as_view(), name='spot_ticket'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),

    # ticket详情页
    url(r'^ticket/detail/(?P<ticket_id>\d+)/$', TicketDetailView.as_view(), name='ticket_detail'),

]
