import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from schedules.forms import UserAskForm
from .models import Spot, Ticket
from operation.models import UserFavorite
# from operation.models import UserFavorite, UserH, CourseComments
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.
from schedules.models import Schedule
from spots.models import Spot

# 课程列表首页
class SpotListView(View):
    def get(self, request):
        all_Spots = Spot.objects.all().order_by('-add_time')
        hot_Spots = Spot.objects.all().order_by('-click_nums')[:3]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_courses = all_Spots.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'students':
            all_courses = all_Spots.order_by('-students')
        elif sort == 'hot':
            all_courses = all_Spots.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_Spots, 3, request=request)
        spots = p.page(page)

        return render(request, 'spots-list.html', {
            'all_spots': spots,
            'hot_spots': hot_Spots,
            'sort': sort,
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

        return render(request, 'spots-detail-homepage.html', {
            'Spot': Spot,
            'relate_courses': relate_spot,
            'has_fav_course': has_fav_Spot,
            'has_fav_org': has_fav_org,
        })

class SpotHomeView(View):
    def get(self, request, spot_id):
        spot = Spot.objects.get(id=int(spot_id))

        # 取出某个指定酒店机构下所有的room(course)
        # 语法 course + _set
        all_rooms = spot.room_set.all()[:3]

        # 初始化判断是否收藏
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=spot.id, fav_type=2):
                has_fav = True

        current_page = 'home'

        return render(request, 'spots-detail-homepage.html', {
            'all_rooms': all_rooms,
            'Spot': Spot,
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
            h = Spot.objects.get(id=fav_id)
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

        return render(request, 'spots-detail-desc.html', {
            'spot': spot,
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

        return render(request, 'spots-detail-ticket.html', {
            'all_rooms': courses,
            'Spot': Spot,
            'current_page': current_page,
            'has_fav': has_fav,
        })
# 课程详情
class TicketDetailView(View):
    def get(self, request, room_id):
        room = Ticket.objects.get(id=int(room_id))

        # 课程点击数 + 1
        room.click_nums += 1
        room.save()

        # 找到相关课程
        tag = room.degree
        relate_rooms = []
        if tag:
            relate_rooms = Ticket.objects.filter(degree=tag)[:2]

        # 课程/机构收藏
        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=room.Spot.id, fav_type=2):
                has_fav_org = True

        return render(request, 'spots-ticket-detail.html', {
            'room': room,
            'relate_courses': relate_rooms,
            'has_fav_course': has_fav_course,
            'has_fav_org': has_fav_org,
        })

