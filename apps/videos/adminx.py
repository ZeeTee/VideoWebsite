# _*_ coding: utf-8 _*_
__date__ = '2018/4/17 下午4:17'

from .models import Video,Lesson,VideoRes

import xadmin


class VideoAdmin(object):
    list_display = ['name', 'desc', 'detail', 'fav_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'fav_nums', 'click_nums', 'add_time']
    list_filter = ['name', 'desc', 'detail', 'fav_nums', 'click_nums', 'add_time']


class LessonAdmin(object):
    list_display = ['video', 'name', 'add_time']
    search_fields = ['video', 'name']
    list_filter = ['video__name', 'name', 'add_time']


class VideoResAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(VideoRes, VideoResAdmin)
