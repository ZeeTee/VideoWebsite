# _*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Video, VideoRes
from operation.models import UserFavorite, VideoComments, UserVideo
from utils.mixin_utils import LoginRequiredMixin
# Create your views here.


class VideoListView(View):
    def get(self, request):
        all_videos = Video.objects.all().order_by("-add_time")
        hot_videos = Video.objects.all().order_by("-click_nums")[:3]

        # 搜索
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_videos = all_videos.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords))  # sql==like
        # 视频排序
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "fav_nums":
                all_videos = all_videos.order_by("-fav_nums")
            elif sort == "hot":
                all_videos = all_videos.order_by("-click_nums")

        # 对视频进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_videos, 3, request=request)
        videos = p.page(page)

        return render(request, 'video-list.html', {
            "all_videos": videos,
            "sort": sort,
            "hot_videos": hot_videos,
            })


class AddFavView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        is_fav = request.POST.get('is_fav', 0)

        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), is_fav=int(is_fav))
        if exist_records:
            # 如果记录已经存在， 则表示用户取消收藏
            exist_records.delete()
            if int(is_fav) == 1:
                video = Video.objects.get(id=int(fav_id))
                video.fav_nums -= 1
                if video.fav_nums < 0:
                    video.fav_nums = 0
                video.save()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(is_fav) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.is_fav = int(is_fav)
                user_fav.save()

                if int(is_fav) == 1:
                    video = Video.objects.get(id=int(fav_id))
                    video.fav_nums += 1
                    video.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')


class VideoDetailView(View):
    """
            课程详情页
    """
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        # 增加视频点击数
        video.click_nums += 1
        video.save()
        #
        tag = video.tag
        if tag:
            relate_videos = Video.objects.filter(tag=tag).exclude(id=int(video_id))[:1]
        else:
            relate_videos = []
        #
        has_fav_video = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=video.id, is_fav=1):
                has_fav_video = True

        return render(request, "video-detail.html", {
            "video": video,
            "relate_videos": relate_videos,
            "has_fav_video": has_fav_video,
        })


class VideoInfoView(LoginRequiredMixin, View):
    """
    章节信息
    """

    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))

        # 查询用户是否已经关联了该视频
        user_videos = UserVideo.objects.filter(user=request.user, video=video)
        if not user_videos:
            user_video = UserVideo(user=request.user, video=video)
            user_video.save()

        user_videos = UserVideo.objects.filter(video=video)
        # 取出所有看过该课程的User_id
        user_ids = [user_video.user.id for user_video in user_videos]
        # user_id 在 User_ids列表中
        all_user_videos = UserVideo.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        video_ids = [user_video.video.id for user_video in all_user_videos]
        # 获取课程
        relate_videos = Video.objects.filter(id__in=video_ids).order_by("-click_nums")[:5]
        return render(request, "video-lesson.html", {
            "video": video,
            "relate_videos": relate_videos,
        })


class CommentsView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        all_comments = VideoComments.objects.all()
        return render(request, "video-comment.html", {
            "video": video,
            "all_comments": all_comments,
        })


class AddComentsView(View):
    """
    用户添加视频评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        video_id = request.POST.get("video_id", 0)
        comments = request.POST.get("comments", "")
        if video_id > 0 and comments:
            video_comments = VideoComments()
            video = Video.objects.get(id=int(video_id))
            video_comments.video = video
            video_comments.comments = comments
            video_comments.user = request.user
            video_comments.save()
            return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')


class VideoPlayView(View):
    """
    视频播放页面
    """
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))

        # 查询用户是否已经关联了该视频
        user_videos = UserVideo.objects.filter(user=request.user, video=video)
        if not user_videos:
            user_video = UserVideo(user=request.user, video=video)
            user_video.save()

        user_videos = UserVideo.objects.filter(video=video)
        # 取出所有看过该课程的User_id
        user_ids = [user_video.user.id for user_video in user_videos]
        # user_id 在 User_ids列表中
        all_user_videos = UserVideo.objects.filter(user_id__in=user_ids)
        # 取出所有课程id
        video_ids = [user_video.video.id for user_video in all_user_videos]
        # 获取课程
        relate_videos = Video.objects.filter(id__in=video_ids).order_by("-click_nums")[:3]

        all_comments = VideoComments.objects.filter(video_id=int(video_id))

        return render(request, "video-play.html", {
            "video": video,
            "relate_videos": relate_videos,
            "all_comments": all_comments,
        })





