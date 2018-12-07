# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from car.models import Brand, Pattern, Car


def index(request):
    return render(request, 'index.html')

def cars(request):
    args = {}
    args['cars'] = Car.objects.all()
    args['brands'] = Brand.objects.all()
    args['patterns'] = Pattern.objects.all()
    return render(request, 'cars.html', args)



