from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^home/$', views.post_home, name='post_home'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^detail/$', views.post_detail, name='post_detail'),
    url(r'^update/$', views.post_update, name='post_update'),
    url(r'^delete/$', views.post_delete, name='post_delete'),
]
