__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import ScheduleListView, ScheduleDetailView, AddFavView

urlpatterns = [
    # 列表页
    url(r'^list/$', ScheduleListView.as_view(), name='schedules_list'),
    url(r'^detail/(?P<schedule_id>\d+)/$', ScheduleDetailView.as_view(), name='schedules_detail'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
