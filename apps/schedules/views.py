import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Schedule
from spots.models import Spot
# Create your views here.


# 课程列表首页
class ScheduleListView(View):
    def get(self, request):
        all_schedules = Schedule.objects.all().order_by('-add_time')
        hot_schedules = Schedule.objects.all().order_by('-click_nums')[:3]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_schedules.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_schedules.order_by('-students')
        elif sort == 'hot':
            all_courses = all_schedules.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_schedules, 3, request=request)
        schedules = p.page(page)

        return render(request, 'schedules-list.html', {
            'all_schedules': schedules,
            'hot_hot_schedules': hot_schedules,
            'sort': sort,
        })
#详情
class ScheduleDetailView(View):
    def get(self, request, course_id):
        schedule = Spot.objects.get(id=int(course_id))

        # 课程点击数 + 1
        schedule.click_nums += 1
        schedule.save()

        # 找到相关课程
        tag = schedule.tag
        relate_schedule = []
        if tag:
            relate_schedule = Spot.objects.filter(tag=tag)[:2]

        # 课程/机构收藏
        has_fav_schedule = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'schedule-detail.html', {
            'schedule': schedule,
            'relate_schedule': relate_schedule,
            'has_fav_schedule': has_fav_schedule,
            'has_fav_org': has_fav_org,
        })

