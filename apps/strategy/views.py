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


class AddFavView(View):

    def set_fav_nums(self, fav_type, fav_id, num=1):
        if fav_type == 1:
            s = Schedule.objects.get(id=fav_id)
            s.fav_nums += num
            s.save()
        elif fav_type == 2:
            h = Hotel.objects.get(id=fav_id)
            h.fav_nums += num
            h.save()
        elif fav_type == 3:
            spot = Spot.objects.get(id=fav_id)
            spot.fav_nums += num
            spot.save()

    def post(self, request):
        fav_id = int(request.POST.get('fav_id', 0))
        fav_type = int(request.POST.get('fav_type', 0))

        res = dict()
        print(fav_id, fav_type)
        if not request.user.is_authenticated():
            res['status'] = 'fail'
            res['msg'] = '用户未登录'
            # return HttpResponse(json.dumps(res), content_type='application/json')
        else:
            print(fav_id, fav_type)
            user_fav = UserFavorite()

            user_fav.user = request.user
            user_fav.fav_id = fav_id
            user_fav.fav_type = fav_type
            user_fav.save()
            self.set_fav_nums(fav_type, fav_id, 1)

            # 发送一条消息
            message_info = ''
            if fav_type == 1:
                message_info = '恭喜您购买 ' + Strategy.objects.filter(id=user_fav.fav_id).first().name + ' 行程成功，祝你出行愉快'
                user_strategy = UserSchedule()
                user_strategy.user = user_fav.user
                user_strategy.strategy = Strategy.objects.filter(id=user_fav.fav_id).first()
                user_strategy.save()
            elif fav_type == 2:
                message_info = '恭喜您预定 ' + Room.objects.filter(id=user_fav.fav_id).first().name + ' 酒店成功，祝你出行愉快'
                user_hotel = UserHotel()
                user_hotel.user = user_fav.user
                user_hotel.hotel = Room.objects.filter(id=user_fav.fav_id).first()
                user_hotel.save()
            elif fav_type == 3:
                message_info = '恭喜您购买 ' + Ticket.objects.filter(id=user_fav.fav_id).first().name + ' 门票成功，祝你出行愉快'
                user_spot = UserSpot()
                user_spot.user = user_fav.user
                user_spot.spot = Ticket.objects.filter(id=user_fav.fav_id).first()
                user_spot.save()

            user_message = UserMessage()
            user_message.user = user_fav.user.id
            user_message.message = message_info
            user_message.has_read = False
            user_message.save()
            res['status'] = 'success'
            res['msg'] = message_info

        # print(user_fav.user,user_fav.fav_id,user_fav.fav_type)
        return HttpResponse(json.dumps(res), content_type='application/json')

