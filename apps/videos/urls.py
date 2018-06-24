# _*_ coding: utf-8 _*_
__date__ = '2018/4/30 下午2:52'

from django.conf.urls import url, include

from .views import VideoListView, VideoDetailView, VideoInfoView, AddFavView, CommentsView, AddComentsView, VideoPlayView

urlpatterns = [
    # 视频列表页
    url(r'^list/$', VideoListView.as_view(), name="video_list"),
    # 视频详情页
    url(r'^detail/(?P<video_id>\d+)/$', VideoDetailView.as_view(), name="video_detail"),
    # 视频章节页
    url(r'^info/(?P<video_id>\d+)/$', VideoInfoView.as_view(), name="video_info"),
    # 收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
    # 视频评论
    url(r'^comment/(?P<video_id>\d+)/$', CommentsView.as_view(), name="video_comments"),
    # 添加视频评论
    url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),
    # 视频播放
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]