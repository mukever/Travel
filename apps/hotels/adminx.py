
import xadmin
from .models import Hotel, Room, BannerHotel

# 添加课程的时候可以顺便添加章节
class RoomInline:
    model = Room
    extra = 0



class HotelAdmin:

    list_display = ['name', 'desc', 'detail', 'degree', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'fav_nums', 'click_nums', 'add_time']

    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']

    #Inline # 添加课程的时候可以顺便添加章节、课程资源
    inlines = [RoomInline]

    style_fields = {'detail': 'ueditor'}

    #重新在这里写一遍的原因是，避免数据重复
    def queryset(self):
        qs = super(HotelAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerHotelAdmin(object):
    style_fields = {'detail': 'ueditor'}
    list_display = ['name', 'desc', 'detail', 'degree', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree',  'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'fav_nums',
                    'click_nums', 'add_time']
    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']

    #Inline # 添加课程的时候可以顺便添加章节、课程资源
    inlines = [RoomInline]

    #把轮播图从 User model 里转移到 Course model 里
    def queryset(self):
        qs = super(BannerHotelAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class RoomAdmin:
    list_display = ['hotel', 'name', 'add_time']
    search_fields = ['hotel', 'name']
    # course 是一个对象，xadmin 不能搜索，需要指定搜索 course 对象里哪一个属性
    list_filter = ['hotel__name', 'name', 'add_time']



xadmin.site.register(Hotel, HotelAdmin)
xadmin.site.register(BannerHotel, BannerHotelAdmin)
xadmin.site.register(Room, RoomAdmin)

