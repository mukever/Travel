"""imooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件

from Travel.settings import MEDIA_ROOT

# from django.contrib import admin
import xadmin

# from users.views import user_login
# from users.views import IndexView
# from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    # url(r'^$', IndexView.as_view(), name="index"),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),


]

# 全局 404 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'


if settings.DEBUG:
    # debug_toolbar 插件配置
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))
else:
    # 项目部署上线时使用
    from Travel.settings import STATIC_ROOT
    # 配置静态文件访问处理
    urlpatterns.append(url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}))