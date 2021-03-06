from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from qinziyou.models import Qinziyou
from zutuanyou.models import Zutuanyou
from .models import UserProfile, EmailVerifyRecord, Banner
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm, UploadImageForm, UserInfoForm
from utils.email_send import send_register_email
from utils.mixin_utils import LoginRequiredMixin
from operation.models import UserMessage, UserQinziyou, UserZutuanyou
from hotels.models import Hotel, BannerHotel, Room
from spots.models import Spot, BannerSpot, Ticket
from schedules.models import Schedule,BannerSchedule
from operation.models import UserHotel,UserSchedule,UserSpot
from operation.models import UserFavorite
import json

# Create your views here.


# 让用户可以用邮箱登录
# setting 里要有对应的配置
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 用户登录（已废弃）
def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 上面的 authenticate 方法 return user
        user = authenticate(username=user_name, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'index.html')
            return render(request, 'login.html', {'msg': '用户未激活！'})
        return render(request, 'login.html', {'msg': '用户名或者密码错误！'})

    elif request.method == 'GET':
        return render(request, 'login.html')


# 用户登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            # 上面的 authenticate 方法 return user
            user = authenticate(username=user_name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponsePermanentRedirect(reverse('index'))
                return render(request, 'login.html', {'msg': '用户未激活！'})
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})

        return render(request, 'login.html', {'form_errors': login_form.errors})


#用户登出
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse('index'))
    def post(self, request):
        logout(request)
        return HttpResponsePermanentRedirect(reverse('index'))


# 用户注册
class RegisterView(View):
    def get(self, request):
        # get 请求的时候，把验证码组件一系列的 HTML render 到 register.html 里
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已经存在！'})
            password = request.POST.get('password', '')

            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()

            #注册时发送一条消息
            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = '欢迎注册驴友在线网！'
            user_message.save()

            send_register_email(email, 'register')
            return render(request, 'send_success.html')

        return render(request, 'register.html', {'register_form': register_form})


# 验证用户注册后，在邮件里点击注册链接
class ActiveUserView(View):
    def get(self, request, active_code):
        # 为什么用 filter ？ 因为用户可能注册了好多次，一个 email 对应了好多个 code
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        return render(request, 'active_fail.html')


# 忘记密码页面
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, 'forget')
            return render(request, 'send_success.html')
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})


# 用户进入到重置密码页面
class ResetView(View):
    def get(self, request, active_code):
        # 如果第二次进来，链接就失效
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for records in all_records:
                email = records.email
                return render(request, 'password_reset.html', {'email': email})
        return render(request, 'active_fail.html')


# 用户在重置密码页面提交新密码
class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        email = request.POST.get('email', '')
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致！'})
            try:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return render(request, 'login.html')
            except  UserProfile.DoesNotExist:
                return render(request, 'password_reset.html', {'email': email, 'msg': '用户不存在！'})
        return render(request, 'password_reset.html', {'email': email, 'modify_form': modify_form})


# userprofile
class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'usercenter/usercenter-info.html')

    # 用户修改昵称，手机号，地址，生日
    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)
        res = dict()

        if user_info_form.is_valid():
            user_info_form.save()
            res['status'] = 'success'

        else:
            res = user_info_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')


# 用户修改头像
class UploadImageView(LoginRequiredMixin, View):
    def post(self, request):
        # image_form = UploadImageForm(request.POST, request.FILES)
        # if image_form.is_valid():
        #     image = image_form.cleaned_data['image']
        #     request.user.image = image
        #     request.user.save()
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        res = dict()
        if image_form.is_valid():
            image_form.save()
            res['status'] = 'success'
            res['msg'] = '头像修改成功'
        else:
            res['status'] = 'fail'
            res['msg'] = '头像修改失败'
        return HttpResponse(json.dumps(res), content_type='application/json')


#用户修改密码
# 用户在个人中心修改密码
class UpdatePwdView(LoginRequiredMixin, View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        res = dict()

        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                res['status'] = 'fail'
                res['msg'] = '两次密码不一致'
                return HttpResponse(json.dumps(res), content_type='application/json')

            user = request.user
            user.password = make_password(pwd2)
            user.save()

            res['status'] = 'success'
            res['msg'] = '密码修改成功'
        else:
            res = modify_form.errors

        return HttpResponse(json.dumps(res), content_type='application/json')


# 发送修改邮箱时的邮箱验证码
class SendEmailCodeView(LoginRequiredMixin, View):
    def get(self, request):
        email = request.GET.get('email', '')

        res = dict()
        if UserProfile.objects.filter(email=email):
            res['email'] = '邮箱已注册'
            return HttpResponse(json.dumps(res), content_type='application/json')
        send_register_email(email, 'update_email')
        res['status'] = 'success'
        res['msg'] = '发送验证码成功'
        return HttpResponse(json.dumps(res), content_type='application/json')


# 修改个人邮箱
class UpdateEmailView(LoginRequiredMixin, View):
    def post(self, request):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')

        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        res = dict()
        if existed_records:
            user = request.user
            user.email = email
            user.save()
            res['status'] = 'success'
            res['msg'] = '邮箱修改成功！'
        else:
            res['status'] = 'fail'
            res['msg'] = '验证码出错！'

        return HttpResponse(json.dumps(res), content_type='application/json')



class MyHotelView(LoginRequiredMixin, View):
    def get(self, request):
     user_hotel = UserHotel.objects.filter(user=request.user)
     return render(request, 'usercenter/usercenter-my.html', {
         'user_hotel': user_hotel,
     })



class MyFavScheduleView(LoginRequiredMixin, View):
    def get(self, request):
        res = []
        fav_rooms = UserFavorite.objects.filter(user=request.user, fav_type=1).values('fav_id')
        for fav_room in fav_rooms:
            temp = Schedule.objects.filter(id=fav_room['fav_id'])
            for te in temp:
                res.append(te)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(res, 3, request=request)
        res = p.page(page)
        return render(request, 'usercenter/usercenter-fav-schedule.html', {
            'org_list': res,
        })

class MyFavQinziyouView(LoginRequiredMixin, View):
    def get(self, request):
        res = []
        fav_rooms = UserFavorite.objects.filter(user=request.user, fav_type=5).values('fav_id')
        for fav_room in fav_rooms:
            temp = Qinziyou.objects.filter(id=fav_room['fav_id'])
            for te in temp:
                res.append(te)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(res, 3, request=request)
        res = p.page(page)
        return render(request, 'usercenter/usercenter-fav-qinziyou.html', {
            'org_list': res,
        })

class MyFavZutuanyouView(LoginRequiredMixin, View):
    def get(self, request):
        res = []
        fav_rooms = UserFavorite.objects.filter(user=request.user, fav_type=4).values('fav_id')
        for fav_room in fav_rooms:
            temp = Zutuanyou.objects.filter(id=fav_room['fav_id'])
            for te in temp:
                res.append(te)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(res, 3, request=request)
        res = p.page(page)
        return render(request, 'usercenter/usercenter-fav-zutuanyou.html', {
            'org_list': res,
        })


class MyFavHotelView(LoginRequiredMixin, View):
    def get(self, request):
        res = []
        fav_rooms = UserFavorite.objects.filter(user=request.user, fav_type=2).values('fav_id')
        for fav_room in fav_rooms:

            temp = Room.objects.filter(id = fav_room['fav_id'])
            for te in temp:
                res.append(te)
                # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(res, 3, request=request)
        res = p.page(page)


        return render(request, 'usercenter/usercenter-fav-hotel.html', {
         'org_list': res,
        })




class MyFavSpotView(LoginRequiredMixin, View):
    def get(self, request):
        res = []
        fav_rooms = UserFavorite.objects.filter(user=request.user, fav_type=3).values('fav_id')
        for fav_room in fav_rooms:

            temp = Ticket.objects.filter(id=fav_room['fav_id'])
            for te in temp:
                res.append(te)


        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(res, 3, request=request)
        res = p.page(page)


        return render(request, 'usercenter/usercenter-fav-spot.html', {
            'org_list': res,
        })



#我的消息
class MyMessageView(LoginRequiredMixin, View):
    def get(self, request):
        # 如果 user = 0 ，代表全局消息，所有用户都能收到
        all_message = UserMessage.objects.filter(user=request.user.id).order_by('-add_time')

        #进入到我的消息页面后，把已读的消息清空
        all_unread_message = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_message:
            unread_message.has_read = True
            unread_message.save()

        # 对个人消息分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_message, 4, request=request)
        messages = p.page(page)

        return render(request, 'usercenter/usercenter-message.html', {
            'messages': messages,
        })


# 驴友在线网首页
class IndexView(View):
    def get(self, request):
        # 取出轮播图
        all_banners = Banner.objects.all().order_by('index')
        schedules = Schedule.objects.filter(is_banner=False)[:6]
        banner_schedules = Schedule.objects.filter(is_banner=True)[:3]
        spots = Spot.objects.all()[:15]

        hotels = Hotel.objects.all()[:15]
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'schedules': schedules,
            'banner_schedules': banner_schedules,
            'spots': spots,
            'hotels': hotels,
        })



# 全局 404 处理函数
def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


# 全局 500 处理函数
def page_error(request):
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response