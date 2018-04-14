import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from hotels.models import Room, Hotel
from operation.models import UserSpot, UserHotel, UserSchedule, UserMessage, UserFavorite
from .models import Schedule
from spots.models import Spot, Ticket


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
        if sort == 'fav_nums':
            all_courses = all_schedules.order_by('-fav_nums')
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
            'hot_schedules': hot_schedules,
            'sort': sort,
        })
#详情
class ScheduleDetailView(View):
    def get(self, request, schedule_id):
        schedule = Schedule.objects.get(id=int(schedule_id))

        # 课程点击数 + 1
        schedule.click_nums += 1
        schedule.save()

        # 找到相关课程
        tag = schedule.tag

        relate_schedules = Schedule.objects.all().order_by('-click_nums')[:3]

        # 课程/机构收藏
        has_fav_schedule = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'schedules-detail.html', {
            'schedule': schedule,
            'relate_schedule': relate_schedules,
            'has_fav_schedule': has_fav_schedule,
            'has_fav_org': has_fav_org,
        })


class AddFavView(View):
    def set_fav_nums(self, fav_type, fav_id, num=1):
        if fav_type == 1:
            s = Schedule.objects.get(id=fav_id)
            s.fav_nums += num
            s.save()
        elif fav_type == 2:
            h = Room.objects.get(id=fav_id)
            h.fav_nums += num
            h.save()
        elif fav_type == 3:
            spot = Ticket.objects.get(id=fav_id)
            spot.fav_nums += num
            spot.save()

    def post(self, request):
        fav_id = int(request.POST.get('fav_id', 0))
        fav_type = int(request.POST.get('fav_type', 0))

        res = dict()
        if not request.user.is_authenticated():
            res['status'] = 'fail'
            res['msg'] = '用户未登录'
            return HttpResponse(json.dumps(res), content_type='application/json')

        user_fav = UserFavorite()
        if fav_id and fav_type:
            user_fav.user = request.user
            user_fav.fav_id = fav_id
            user_fav.fav_type = fav_type
            user_fav.save()
            self.set_fav_nums(fav_type, fav_id, 1)

            # 发送一条消息
            message_info = ''
            if fav_type == 1:
               message_info = '恭喜您购买 '+Schedule.objects.filter(id=user_fav.fav_id).first().name+' 行程成功，祝你出行愉快'
               user_schedule = UserSchedule()
               user_schedule.user = user_fav.user
               user_schedule.schedule = Schedule.objects.filter(id=user_fav.fav_id).first()
               user_schedule.save()
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

        else:
            res['status'] = 'fail'
            res['msg'] = '购买出错'
        print(user_fav.user,user_fav.fav_id,user_fav.fav_type)
        return HttpResponse(json.dumps(res), content_type='application/json')

