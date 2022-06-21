from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # используем уже готовый класс выхода

import telebot
from .views import *
from telebot.views import *

urlpatterns = [
    path('', BlogHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),


    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('login/', LoginUser.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('contact/', contact_page, name='contact'),
    path('thanks/', thanks_page, name='thanks_page')

]
