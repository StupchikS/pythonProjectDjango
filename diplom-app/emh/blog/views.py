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


class IndexHome(DataMixin, ListView):

    model = Index
    template_name = 'blog/index.html'
    context_object_name = 'index'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):

        return Index.objects.all()


class BlogHome(DataMixin, ListView):
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


class ShowPost(DataMixin, DetailView):
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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/getinfo.html'
    success_url = reverse_lazy('index')  # куда идти после успешного заполнения формы
    login_url = reverse_lazy('index')  # если пользователь не зарегился куда его

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить статью')
        return dict(list(context.items()) + list(c_def.items()))


# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'blog/register.html'
#     success_url = reverse_lazy('login')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Регистрация')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('index')
#
# #
# class LoginUser(DataMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'blog/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Авторизация')
#         return dict(list(context.items()) + list(c_def.items()))

#
# class ContactFormView(DataMixin, FormView):
#     form_class = ContactForm
#     template_name = 'blog/contact.html'
#     success_url = reverse_lazy('index')  # заполнили форму связи и куда далее
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Обратная связь')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def form_valid(self, form):
#         print(form.cleaned_data)  # временное решение, соберет заполненные данные
#         subject = 'Message'
#         body = {
#             'name': form.cleaned_data['name'],
#             'email': form.cleaned_data['email'],
#             'content': form.cleaned_data['content'],
#         }
#         message = '\n'.join(body.values())
#         try:
#             send_mail(subject, message, form.cleaned_data['email'], ['admin@log.ru'])
#         except BadHeaderError:
#             return HttpResponse('Найден некорректный заголовок')
#         return redirect('index')


def contact_page(request):

    form = OrderForm()

    dict_obj = {

        'form': form,
    }
    return render(request, 'blog/contact.html', dict_obj)


def thanks_page(request):
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