
import xadmin
from .models import Schedule, BannerSchedule




class ScheduleAdmin:

    list_display = ['name', 'desc',  'category', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc',  'category', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc',  'category', 'fav_nums', 'click_nums', 'add_time']

    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']


    style_fields = {'detail': 'ueditor'}

    #重新在这里写一遍的原因是，避免数据重复
    def queryset(self):
        qs = super(ScheduleAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerScheduleAdmin(object):

    list_display = ['name', 'desc', 'detail', 'category', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'category',  'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'category', 'fav_nums',
                    'click_nums', 'add_time']
    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    style_fields = {'detail': 'ueditor'}

    #把轮播图从 User model 里转移到 Course model 里
    def queryset(self):
        qs = super(BannerScheduleAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs



xadmin.site.register(Schedule, ScheduleAdmin)
xadmin.site.register(BannerSchedule, BannerScheduleAdmin)

