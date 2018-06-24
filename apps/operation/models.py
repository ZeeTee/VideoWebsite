# _*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from users.models import UserProfile
from videos.models import Video

# Create your models here.


class VideoComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    video = models.ForeignKey(Video, verbose_name=u"视频")
    comments = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"视频id")
    is_fav = models.IntegerField(default=0, verbose_name=u"收藏")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u"接受用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"消息时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserVideo(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    video = models.ForeignKey(Video, verbose_name=u"视频")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户观看"
        verbose_name_plural = verbose_name



