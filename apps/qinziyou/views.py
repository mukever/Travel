import json

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from hotels.models import Room, Hotel
from operation.models import UserSpot, UserHotel, UserSchedule, UserMessage, UserFavorite, UserQinziyou
from .models import Qinziyou
from spots.models import Spot, Ticket


# Create your views here.


# 课程列表首页
class QinziyouListView(View):
    def get(self, request):
        all_qinziyous = Qinziyou.objects.all().order_by('-add_time')
        hot_qinziyous = Qinziyou.objects.all().order_by('-click_nums')[:2]

        #课程搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            all_qinziyous = all_qinziyous.filter(
                Q(name__icontains=search_keywords) |
                Q(desc__icontains=search_keywords) |
                Q(detail__icontains=search_keywords)
            )

        # 课程排序
        sort = request.GET.get('sort', '')
        if sort == 'fav_nums':
            all_qinziyous = all_qinziyous.order_by('-fav_nums')
        elif sort == 'hot':
            all_qinziyous = all_qinziyous.order_by('-click_nums')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_qinziyous, 6, request=request)
        qinziyous = p.page(page)

        return render(request, 'qinziyou/qinziyous-list.html', {
            'all_qinziyous': qinziyous,
            'hot_qinziyous': hot_qinziyous,
            'sort': sort,
        })
#详情
class QinziyouDetailView(View):
    def get(self, request, qinziyou_id):
        qinziyou = Qinziyou.objects.get(id=int(qinziyou_id))

        # 课程点击数 + 1
        qinziyou.click_nums += 1
        qinziyou.save()

        # 找到相关课程
        tag = qinziyou.tag

        relate_qinziyous = Qinziyou.objects.all().order_by('-click_nums')[:3]

        # 课程/机构收藏
        has_fav_qinziyou = False
        has_fav_org = False
        # if request.user.is_authenticated():
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
        #         has_fav_course = True
        #     if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
        #         has_fav_org = True

        return render(request, 'qinziyou/qinziyou-detail.html', {
            'qinziyou': qinziyou,
            'relate_qinziyous': relate_qinziyous,
            'has_fav_qinziyou': has_fav_qinziyou,
            'has_fav_org': has_fav_org,
        })


class AddFavView(View):

    def set_fav_nums(self, fav_type, fav_id, num=1):
        if fav_type == 5:
            s = Qinziyou.objects.get(id=fav_id)
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
            self.set_fav_nums(fav_type, fav_id, 1)

            # 发送一条消息
            message_info = ''
            if fav_type == 5:
                message_info = '恭喜您购买 ' + Qinziyou.objects.filter(id=user_fav.fav_id).first().name + ' 成功，祝你出行愉快'
                user_qinziyou = UserQinziyou()
                user_qinziyou.user = user_fav.user
                user_qinziyou.qinziyou = Qinziyou.objects.filter(id=user_fav.fav_id).first()
                user_qinziyou.save()


            user_message = UserMessage()
            user_message.user = user_fav.user.id
            user_message.message = message_info
            user_message.has_read = False
            user_message.save()
            res['status'] = 'success'
            res['msg'] = message_info

        # print(user_fav.user,user_fav.fav_id,user_fav.fav_type)
        return HttpResponse(json.dumps(res), content_type='application/json')

