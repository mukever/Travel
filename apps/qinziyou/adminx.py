
import xadmin
from .models import Qinziyou




class QinziyouAdmin:

    list_display = ['name', 'desc',  'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc',   'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'fav_nums', 'click_nums', 'add_time']

    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']


    style_fields = {'detail': 'ueditor'}

    #重新在这里写一遍的原因是，避免数据重复
    def queryset(self):
        qs = super(QinziyouAdmin, self).queryset()
        return qs


xadmin.site.register(Qinziyou, QinziyouAdmin)

