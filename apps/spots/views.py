import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Spot
# from operation.models import UserFavorite, UserH, CourseComments
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


# 课程列表首页
class SpotListView(View):
    def get(self, request):
        all_spots = Spot.objects.all().order_by('-add_time')
        hot_spots = Spot.objects.all().order_by('-click_nums')[:3]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_spots.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_spots.order_by('-students')
        elif sort == 'hot':
            all_courses = all_spots.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_spots, 3, request=request)
        spots = p.page(page)

        return render(request, 'spots-list.html', {
            'all_spots': spots,
            'hot_spots': hot_spots,
            'sort': sort,
        })
#详情
class SpotsDetailView(View):
    def get(self, request, course_id):
        spot = Spot.objects.get(id=int(course_id))

        # 课程点击数 + 1
        spot.click_nums += 1
        spot.save()

        # 找到相关课程
        tag = spot.tag
        relate_spot = []
        if tag:
            relate_courses = Spot.objects.filter(tag=tag)[:2]

        # 课程/机构收藏
        has_fav_spot = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'spot-detail.html', {
            'hotel': spot,
            'relate_spot': relate_spot,
            'has_fav_spot': has_fav_spot,
            'has_fav_org': has_fav_org,
        })
