# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from car.models import Brand, Pattern, Category, Car


def index(request):
    return render(request, 'index.html')

def cars(request):
    args = {}
    args['cars'] = Car.objects.all()
    args['brands'] = Brand.objects.all()
    args['patterns'] = Pattern.objects.all()
    args['projects'] = Category.objects.all()
    return render(request, 'cars.html', args)


def car_cat(request, category_id=1):
    args = {}
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['cars'] = Car.objects.filter(category_id=category_id)
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_cars'] = Car.objects.filter(category__in=branch_categories).distinct()
    return render(request, 'car_cat.html', args)



