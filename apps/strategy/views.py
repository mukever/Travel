import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from hotels.models import Room, Hotel
from operation.models import UserSpot, UserHotel, UserMessage, UserFavorite, UserSchedule
from schedules.models import Schedule
from spots.models import Spot, Ticket
from .models import Strategy

# Create your views here.

class StrategyListView(View):
    def get(self, request):
        all_strategy = Strategy.objects.all().order_by('-add_time')
        hot_strategy = Strategy.objects.all().order_by('-click_nums')[:2]

        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_strategy = all_strategy.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        sort = request.GET.get('sort', '')
        if sort == 'fav_nums':
            all_strategy = all_strategy.order_by('-fav_nums')
        elif sort == 'hot':
            all_strategy = all_strategy.order_by('-click_nums')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_strategy, 6, request=request)
        strategy = p.page(page)

        return render(request, 'strategy/strategys-list.html', {
            'all_strategys': strategy,
            'hot_strategys': hot_strategy,
            'sort': sort,
        })


class StrategyDetailView(View):
    def get(self, request, strategy_id):
        strategy = Strategy.objects.get(id=int(strategy_id))

        # 课程点击数 + 1
        strategy.click_nums += 1
        strategy.save()
        # 找到相关课程
        tag = strategy.tag

        relate_strategy = Strategy.objects.all().order_by('-click_nums')[:3]

        # 课程/机构收藏
        has_fav_strategy = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'strategy/strategy-detail.html', {
            'strategy': strategy,
            'relate_strategy': relate_strategy,
            'has_fav_strategy': has_fav_strategy,
            'has_fav_org': has_fav_org,
        })
