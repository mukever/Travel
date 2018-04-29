
import xadmin
from .models import Strategy

class StrategyAdmin:

    list_display = ['name', 'desc', 'detail', 'category', 'fav_nums',
                    'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'category', 'fav_nums',
                    'click_nums']
    list_filter = ['name', 'desc', 'detail', 'category', 'fav_nums', 'click_nums', 'add_time']

    ordering = ['-click_nums']

    # readonly_fields 和 exclude 的字段不要重复，否则会冲突
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']

    style_fields = {'detail': 'ueditor'}



xadmin.site.register(Strategy, StrategyAdmin)

