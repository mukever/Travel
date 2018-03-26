__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import CourseListView,HotelDetailView
    #CourseDetailView, CourseInfoView, CommentView, AddCommentView, VideoPlayView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='hotels_list'),
    # 课程详情页
    url(r'^detail/(?P<hotel_id>\d+)/$', HotelDetailView.as_view(), name='hotel_detail'),
]
