
import xadmin
from .models import Spot, Ticket, CityDict

class TicketInline:
    model = Ticket
    extra = 0

class CityDictAdmin:
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']



class SpotsAdmin:
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']

    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']

    #Inline
    inlines = [TicketInline]

    #重新在这里写一遍的原因是，避免数据重复
    def queryset(self):
        qs = super(SpotsAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class TicketsAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums',
                    'click_nums', 'add_time']
    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']

    #把轮播图从 User model 里转移到 Course model 里
    def queryset(self):
        qs = super(TicketsAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Spot, SpotsAdmin)
xadmin.site.register(Ticket, TicketsAdmin)

