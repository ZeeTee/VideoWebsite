# -*- coding: utf-8 -*-
"""pyvideos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView
from pyvideos.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
    url('^index/$', IndexView.as_view(), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url('^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # 视频相关URL配置
    url(r'^video/', include('videos.urls', namespace="video")),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 当debug模式关闭时，Django不再代理静态文件，自己配置静态文件
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),

    # 用户相关URL配置
    url(r'^users/', include('users.urls', namespace="users")),


]

# 全局404配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
