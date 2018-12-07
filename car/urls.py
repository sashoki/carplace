from django.conf.urls import url, include
from django.contrib import admin
from car.views import cars, car_cat

urlpatterns = [

    url(r'^category/get/(?P<category_id>\d+)/$', car_cat, name='car_cat'),
    url(r'^$', cars, name='cars'),

    ]

