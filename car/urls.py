from django.conf.urls import url, include
from django.contrib import admin
from car.views import cars

urlpatterns = [
    url(r'^$', cars, name='cars'),
    ]

