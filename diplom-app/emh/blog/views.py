from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, CreateView, FormView
from emh.utils import *  #  добавляем миксин, в классе идет первым
from .models import *
from .forms import *
from django.urls import reverse_lazy  #  переадресация
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from crm.models import Order
from telebot.sendmessage import send_telegram
from crm.forms import OrderForm


class IndexHome(DataMixin, ListView):  #  обрабатывает гл страницу, берет из бд данные больницы

    model = Index
    template_name = 'blog/index.html'
    context_object_name = 'index'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return Index.objects.all()


class BlogHome(DataMixin, ListView):  #  обрабатывает страницу чс новостями больницы
    paginate_by = 4  # из listview сколько отображать на странице
    model = Blog
    template_name = 'blog/posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Новости больницы')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return Blog.objects.filter(is_published=True)


class ShowPost(DataMixin, DetailView):  #  показывает новость в отдельном окне каждую выбраную
    model = Blog
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


def contact_page(request):  #  формирует страницу для сообщений в телебот

    form = OrderForm()

    dict_obj = {

        'form': form,
    }
    return render(request, 'blog/contact.html', dict_obj)


def thanks_page(request):  #  страница ни о чем чтобы пользователь понял, что его сообщение ушло
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        context = request.POST['context']
        element = Order(order_name=name, order_phone=phone, order_email=email, order_context=context)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, 'blog/thanks.html', {'name': name})
    else:
        return render(request, 'blog/thanks.html')