# _*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=50, verbose_name=u"视频名")
    desc = models.CharField(max_length=300, verbose_name=u"视频描述")
    detail = models.TextField(verbose_name=u"视频详情")
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    times = models.IntegerField(default=0, verbose_name=u"视频时长")
    plays = models.IntegerField(default=0, verbose_name=u"播放次数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    category = models.CharField(default=u"开发", max_length=20, verbose_name=u"视频分类")
    image = models.ImageField(upload_to="videos/%Y/%m", verbose_name=u"封面图")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    tag = models.CharField(default="", verbose_name=u"视频标签", max_length=20)
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")

    class Meta:
        verbose_name = u"视频信息"
        verbose_name_plural = verbose_name

    def get_fj_nums(self):
        # 获取分集数
        return self.lesson_set.all().count()

    def get_play_users(self):
        return self.uservideo_set.all()[:5]

    def get_video_lesson(self):
        # 获取视频章节数
        return self.lesson_set.all()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    video = models.ForeignKey(Video, verbose_name=u"所属视频")
    name = models.CharField(max_length=100, verbose_name=u"分集名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"分集"
        verbose_name_plural = verbose_name

    def get_lesson_video(self):
        # 获取章节视频数
        return self.videores_set.all()

    def __unicode__(self):
        return self.name


class VideoRes(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"所属分集")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    times = models.IntegerField(default=0, verbose_name=u"时长")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

