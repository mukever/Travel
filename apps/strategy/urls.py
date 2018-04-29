__author__ = 'zaxlct'
__date__ = '2017/4/7 上午9:58'

from django.conf.urls import url
from .views import StrategyListView, StrategyDetailView, AddFavView

urlpatterns = [
    # 列表页
    url(r'^list/$', StrategyListView.as_view(), name='strategys_list'),
    url(r'^detail/(?P<strategy_id>\d+)/$', StrategyDetailView.as_view(), name='strategys_detail'),
    # 收藏/取消收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
