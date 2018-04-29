__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import QinziyouListView, QinziyouDetailView, AddFavView

urlpatterns = [
    # 列表页
    url(r'^list/$', QinziyouListView.as_view(), name='qinziyous_list'),
    url(r'^detail/(?P<qinziyou_id>\d+)/$', QinziyouDetailView.as_view(), name='qinziyous_detail'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
