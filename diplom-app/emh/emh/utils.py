from blog.models import *
from django.db.models import Count


menu = [

    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Новости Больницы", 'url_name': 'posts'},
    {'title': "Администрация Больницы", 'url_name': 'person'},

]


class DataMixin:
    paginate_by = 4  # из listview сколько отображать на странице

    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)

        context['menu'] = user_menu

        return context