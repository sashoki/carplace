# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from car.models import Brand, Pattern, Category, Car


def index(request):
    return render(request, 'index.html')

def cars(request,  car_id=1):
    args = {}
    args['cars'] = Car.objects.all()
    args['brands'] = Brand.objects.all()
    args['patterns'] = Pattern.objects.all()
    args['caregory'] = Category.objects.filter(id=car_id)
    return render(request, 'cars.html', args)



