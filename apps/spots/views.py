import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from hotels.models import Hotel, Room
from .models import Spot, Ticket, CityDict
from operation.models import UserFavorite, UserMessage, UserSchedule, UserHotel, UserSpot
# from operation.models import UserFavorite, UserH, CourseComments
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.
from schedules.models import Schedule
from spots.models import Spot

# 课程列表首页
class SpotListView(View):
    def get(self, request):
        all_citys = CityDict.objects.all()
        all_Spots = Spot.objects.all().order_by('-add_time')
        hot_Spots = Spot.objects.all().order_by('-click_nums')[:6]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_Spots = all_Spots.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )
        # print('cat'+request.GET.get('ct'))
        if request.GET.get('ct') is not None and request.GET.get('ct') !='':
            # print(request.GET.get('ct'))
            all_Spots = all_Spots.filter(category=request.GET.get('ct'))
        if request.GET.get('city') is not None and request.GET.get('city') !='':
            # print(request.GET.get('city'))
            all_Spots = all_Spots.filter(city=request.GET.get('city'))
        # 课程排序
        # print(all_Spots.__len__())
        sort = request.GET.get('sort', '')
        if sort == 'visit':
            all_Spots = all_Spots.order_by('-visit_nums')
        elif sort == 'buy':
            all_Spots = all_Spots.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_Spots, 3, request=request)
        all_Spots = p.page(page)


        return render(request, 'spot/spots-list.html', {
            'all_spots': all_Spots,
            'hot_spots': hot_Spots,
            'sort': sort,
            'all_citys': all_citys,
        })


#详情
class SpotDetailView(View):
    def get(self, request, spot_id):
        spot = Spot.objects.get(id=int(spot_id))

        # 课程点击数 + 1
        spot.click_nums += 1
        spot.save()

        # 找到相关课程
        tag = spot.tag
        relate_spot = []
        if tag:
            relate_courses = Spot.objects.filter(tag=tag)[:2]

        # 课程/机构收藏
        has_fav_Spot = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'spot/spots-detail-homepage.html', {
            'spot': Spot,
            'relate_courses': relate_spot,
            'has_fav_course': has_fav_Spot,
            'has_fav_org': has_fav_org,
        })

class SpotHomeView(View):
    def get(self, request, spot_id):
        spot = Spot.objects.get(id=int(spot_id))

        # 取出某个指定酒店机构下所有的room(course)
        # 语法 course + _set
        all_tickets = spot.ticket_set.all()[:3]

        # 初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=spot.id, fav_type=2):
                has_fav = True

        current_page = 'home'

        return render(request, 'spot/spots-detail-homepage.html', {
            'all_tickets': all_tickets,
            'spot': spot,
            'current_page': current_page,
            'has_fav': has_fav,
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
                message_info = '恭喜您购买 ' + Schedule.objects.filter(id=user_fav.fav_id).first().name + ' 行程成功，祝你出行愉快'
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

        # print(user_fav.user,user_fav.fav_id,user_fav.fav_type)
        return HttpResponse(json.dumps(res), content_type='application/json')



class SpotDescView(View):
    # 课程机构介绍页
    def get(self, request, spot_id):
        current_page = 'desc'
        spot = Spot.objects.get(id=int(spot_id))

        # 初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=spot.id, fav_type=2):
                has_fav = True

        return render(request, 'spot/spots-detail-desc.html', {
            'spot': spot,
            'current_page': current_page,
            'has_fav': has_fav,
        })


# 课程机构详情页讲师页面
class SpotTicketView(View):
    def get(self, request, spot_id):
        current_page = 'Spot'
        spot = Spot.objects.get(id=int(spot_id))
        all_rooms = spot.ticket_set().all()

        #初始化判断是否收藏
        has_fav = False
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_rooms, 2, request=request)

        courses = p.page(page)

        return render(request, 'spot/spots-detail-ticket.html', {
            'all_rooms': courses,
            'spot': Spot,
            'current_page': current_page,
            'has_fav': has_fav,
        })
# 课程详情
class TicketDetailView(View):
    def get(self, request, ticket_id):
        ticket = Ticket.objects.get(id=int(ticket_id))
        relate_tickets = Ticket.objects.all().order_by('-click_nums')[:3]
        # 课程点击数 + 1
        ticket.click_nums += 1
        ticket.save()


        # 课程/机构收藏
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=ticket.org.id, fav_type=2):
                has_fav_org = True

        return render(request, 'spot/spots-ticket-detail.html', {
            'ticket': ticket,
            'relate_tickets': relate_tickets,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })

