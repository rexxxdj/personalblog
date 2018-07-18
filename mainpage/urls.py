from django.urls import path
from django.conf.urls import include, url
from mainpage import views

urlpatterns = [
    url(r'^$', views.mainpage_list, name='home'),
    ]