__author__ = 'zaxlct'
__date__ = '2017/4/9 上午11:55'

from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyFavSpotView, \
    MyFavScheduleView
from .views import MyMessageView
from .views import MyHotelView,MyFavHotelView
urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户头像修改
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),

    # 修改邮箱时 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 修改邮箱时，验证邮箱和验证码
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),


    # 我的酒店
    url(r'^myhotel/$', MyHotelView.as_view(), name='myhotel'),

    # 我收藏
    url(r'^myfav/hotel/$', MyFavHotelView.as_view(), name='myfav_hotel'),
    # 我收藏
    url(r'^myfav/spot/$', MyFavSpotView.as_view(), name='myfav_spot'),
    # 我收藏
    url(r'^myfav/schedule/$', MyFavScheduleView.as_view(), name='myfav_schedule'),



    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name='mymessage'),
]