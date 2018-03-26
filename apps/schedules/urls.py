__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import ScheduleListView,ScheduleDetailView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', ScheduleListView.as_view(), name='schedules_list'),
    url(r'^detail/(?P<schedule_id>\d+)/$', ScheduleDetailView.as_view(), name='schedule_detail'),

]
