import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from hotels.models import Room, Hotel
from operation.models import UserSpot, UserHotel, UserSchedule, UserMessage, UserFavorite, UserZutuanyou
from .models import Zutuanyou
from spots.models import Spot, Ticket


# Create your views here.


# 课程列表首页
class ZutuanyouListView(View):
    def get(self, request):
        all_zutuanyous = Zutuanyou.objects.all().order_by('-add_time')
        hot_zutuanyous = Zutuanyou.objects.all().order_by('-click_nums')[:2]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_zutuanyous = all_zutuanyous.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'fav_nums':
            all_zutuanyous = all_zutuanyous.order_by('-fav_nums')
        elif sort == 'hot':
            all_zutuanyous = all_zutuanyous.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_zutuanyous, 6, request=request)
        zutuanyous = p.page(page)

        return render(request, 'zutuanyou/zutuanyous-list.html', {
            'all_zutuanyous': zutuanyous,
            'hot_zutuanyous': hot_zutuanyous,
            'sort': sort,
        })
#详情
class ZutuanyouDetailView(View):
    def get(self, request, zutuanyou_id):
        zutuanyou = Zutuanyou.objects.get(id=int(zutuanyou_id))

        # 课程点击数 + 1
        zutuanyou.click_nums += 1
        zutuanyou.save()

        # 找到相关课程
        tag = zutuanyou.tag

        relate_zutuanyous = Zutuanyou.objects.all().order_by('-click_nums')[:3]

        # 课程/机构收藏
        has_fav_zutuanyou = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'zutuanyou/zutuanyou-detail.html', {
            'zutuanyou': zutuanyou,
            'relate_zutuanyous': relate_zutuanyous,
            'has_fav_zutuanyou': has_fav_zutuanyou,
            'has_fav_org': has_fav_org,
        })


class AddFavView(View):

    def set_fav_nums(self, fav_type, fav_id, num=1):
        if fav_type == 4:
            s = Zutuanyou.objects.get(id=fav_id)
            s.fav_nums += num
            s.save()

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
            self.set_fav_nums(fav_type, fav_id, 4)

            # 发送一条消息
            message_info = ''
            if fav_type == 4:
                message_info = '恭喜您购买 ' + Zutuanyou.objects.filter(id=user_fav.fav_id).first().name + ' 成功，祝你出行愉快'
                user_zutuanyou = UserZutuanyou()
                user_zutuanyou.user = user_fav.user
                user_zutuanyou.zutuanyou = Zutuanyou.objects.filter(id=user_fav.fav_id).first()
                user_zutuanyou.save()

            user_message = UserMessage()
            user_message.user = user_fav.user.id
            user_message.message = message_info
            user_message.has_read = False
            user_message.save()
            res['status'] = 'success'
            res['msg'] = message_info

        # print(user_fav.user,user_fav.fav_id,user_fav.fav_type)
        return HttpResponse(json.dumps(res), content_type='application/json')

