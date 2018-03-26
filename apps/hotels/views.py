import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from schedules.forms import UserAskForm
from .models import Hotel, Room
from operation.models import UserFavorite
# from operation.models import UserFavorite, UserH, CourseComments
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.
from schedules.models import Schedule
from spots.models import Spot

# 课程列表首页
class HotelListView(View):
    def get(self, request):
        all_hotels = Hotel.objects.all().order_by('-add_time')
        hot_hotels = Hotel.objects.all().order_by('-click_nums')[:3]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_hotels.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_hotels.order_by('-students')
        elif sort == 'hot':
            all_courses = all_hotels.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_hotels, 3, request=request)
        hotels = p.page(page)

        return render(request, 'hotels-list.html', {
            'all_hotels': hotels,
            'hot_hotels': hot_hotels,
            'sort': sort,
        })


#详情
class HotelDetailView(View):
    def get(self, request, hotel_id):
        hotel = Hotel.objects.get(id=int(hotel_id))

        # 课程点击数 + 1
        hotel.click_nums += 1
        hotel.save()

        # 找到相关课程
        tag = hotel.tag
        relate_hotel = []
        if tag:
            relate_courses = Hotel.objects.filter(tag=tag)[:2]

        # 课程/机构收藏
        has_fav_hotel = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'hotels-detail.html', {
            'hotel': hotel,
            'relate_courses': relate_hotel,
            'has_fav_course': has_fav_hotel,
            'has_fav_org': has_fav_org,
        })

class HotelHomeView(View):
    def get(self, request, hotel_id):
        hotel = Hotel.objects.get(id=int(hotel_id))

        # 取出某个指定酒店机构下所有的room(course)
        # 语法 course + _set
        all_rooms = hotel.room_set.all()[:3]

        # 初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=hotel.id, fav_type=2):
                has_fav = True

        current_page = 'home'

        return render(request, 'hotels-detail-homepage.html', {
            'all_rooms': all_rooms,
            'hotel': hotel,
            'current_page': current_page,
            'has_fav': has_fav,
        })

class AddFavView(View):
    # 用户收藏、取消收藏 课程机构
    # (1, '行程'), (2, '酒店'), (3, '景区') )
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
        if not request.user.is_authenticated():
            res['status'] = 'fail'
            res['msg'] = '用户未登录'
            return HttpResponse(json.dumps(res), content_type='application/json')

        # 查询收藏记录
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=fav_id, fav_type=fav_type)
        if exist_records:
            exist_records.delete()
            self.set_fav_nums(fav_type, fav_id, -1)
            res['status'] = 'success'
            res['msg'] = '收藏'
        else:
            user_fav = UserFavorite()
            if fav_id and fav_type:
                user_fav.user = request.user
                user_fav.fav_id = fav_id
                user_fav.fav_type = fav_type
                user_fav.save()
                self.set_fav_nums(fav_type, fav_id, 1)

                res['status'] = 'success'
                res['msg'] = '已收藏'
            else:
                res['status'] = 'fail'
                res['msg'] = '收藏出错'
        return HttpResponse(json.dumps(res), content_type='application/json')


class HotelDescView(View):
    # 课程机构介绍页
    def get(self, request, hotel_id):
        current_page = 'desc'
        hotel = Hotel.objects.get(id=int(hotel_id))

        # 初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=hotel.id, fav_type=2):
                has_fav = True

        return render(request, 'hotels-detail-desc.html', {
            'hotel': hotel,
            'current_page': current_page,
            'has_fav': has_fav,
        })


# 用户添加咨询课程表单提交
class AddUserAskView(View):
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        res = dict()
        if user_ask_form.is_valid():
            user_ask_form.save(commit=True)
            res['status'] = 'success'
        else:
            res['status'] = 'fail'
            res['msg'] = '添加出错'
        return HttpResponse(json.dumps(res), content_type='application/json')


# 课程机构详情页讲师页面
class HotelRoomView(View):
    def get(self, request, hotel_id):
        current_page = 'hotel'
        hotel = Hotel.objects.get(id=int(hotel_id))
        all_rooms = hotel.room_set.all()

        #初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id = hotel.id, fav_type=2):
                has_fav = True

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_rooms, 2, request=request)

        courses = p.page(page)

        return render(request, 'hotels-detail-room.html', {
            'all_rooms': courses,
            'hotel': hotel,
            'current_page': current_page,
            'has_fav': has_fav,
        })
# 课程详情
class RoomDetailView(View):
    def get(self, request, room_id):
        room = Room.objects.get(id=int(room_id))

        # 课程点击数 + 1
        room.click_nums += 1
        room.save()

        # 找到相关课程
        tag = room.degree
        relate_rooms = []
        if tag:
            relate_rooms = Room.objects.filter(degree=tag)[:2]

        # 课程/机构收藏
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=room.hotel.id, fav_type=2):
                has_fav_org = True

        return render(request, 'hotels-room-detail.html', {
            'room': room,
            'relate_courses': relate_rooms,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })

