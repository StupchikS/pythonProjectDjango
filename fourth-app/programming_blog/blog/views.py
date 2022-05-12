from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

menu = [
    {'title': "Добавить статью", 'url_name': 'index'},
    {'title': "Войти", 'url_name': 'index'}
]


class BlogHome(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['menu'] = menu
        return context


class ShowPost(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context
