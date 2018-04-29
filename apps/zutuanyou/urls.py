__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import ZutuanyouListView, ZutuanyouDetailView, AddFavView

urlpatterns = [
    # 列表页
    url(r'^list/$', ZutuanyouListView.as_view(), name='zutuanyous_list'),
    url(r'^detail/(?P<zutuanyou_id>\d+)/$', ZutuanyouDetailView.as_view(), name='zutuanyous_detail'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
