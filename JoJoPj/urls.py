"""JoJoPj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',        'JoJo.views.homepage', name='login'),
    url(r'^login/$',  'JoJo.views.login', name='login'),
    url(r'^regist/$', 'JoJo.views.regist', name='regist'),
    url(r'^index/$',  'JoJo.views.index', name='index'),
    url(r'^logout/$', 'JoJo.views.logout', name='logout'),
    url(r'^share/$',  'JoJo.views.share', name='share'),

    url(r'^ajax_list/$', 'JoJo.views.ajax_list', name='ajax-list'),
]
