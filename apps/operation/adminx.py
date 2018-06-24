# _*_ coding: utf-8 _*_
__date__ = '2018/4/17 下午5:58'
import xadmin


from .models import UserFavorite,UserMessage,UserVideo,VideoComments


class UserFavAdmin(object):
    list_display = ['user', 'fav_id']
    search_fields = ['user', 'fav_id']
    list_filter = ['user', 'fav_id']


class UserMessAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserVideoAdmin(object):
    list_display = ['user', 'video', 'add_time']
    search_fields = ['user', 'video']
    list_filter = ['user', 'video', 'add_time']


class VideoCommentsAdmin(object):
    list_display = ['user', 'video', 'comments', 'add_time']
    search_fields = ['user', 'video','comments']
    list_filter = ['user', 'video', 'comments', 'add_time']


xadmin.site.register(UserFavorite, UserFavAdmin)
xadmin.site.register(UserMessage, UserMessAdmin)
xadmin.site.register(UserVideo, UserVideoAdmin)
xadmin.site.register(VideoComments, VideoCommentsAdmin)
