"""emh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', BlogHome.as_view(), name='index'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    #
    # path('addpage/', AddPage.as_view(), name='add_page'),
    #
    # path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # path('contact/', ContactFormView.as_view(), name='contact'),
    path('', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    # path('thanks/', telebot.views.thanks_page, name='thanks_page')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
