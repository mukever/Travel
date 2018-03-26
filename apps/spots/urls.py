__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import SpotListView,SpotsDetailView
urlpatterns = [
    # 课程列表页
    url(r'^list/$', SpotListView.as_view(), name='spots_list'),
    url(r'^detail/(?P<spot_id>\d+)/$', SpotsDetailView.as_view(), name='spot_detail'),
]
