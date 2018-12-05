#-*- coding: utf-8 -*-

from django.contrib import admin

from car.models import Brand, Pattern, Car


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', )

class PatternAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', )

class CarAdmin(admin.ModelAdmin):
    fields = ['brand', 'pattern', 'year', 'price', 'owner']
    list_display = ('brand', 'pattern', 'year', 'price', 'owner',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Car, CarAdmin)