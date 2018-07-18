from django.urls import path
from django.conf.urls import include, url
from blog import views

urlpatterns = [
    url(r'^$', views.article_list, name='blog'),
    ]