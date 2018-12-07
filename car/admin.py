#-*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from car.models import Brand, Pattern, Category, Car


# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', )


class PatternAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']


class CarAdmin(admin.ModelAdmin):
    fields = ['brand', 'pattern', 'year', 'category', 'price', 'owner']
    list_display = ('id', 'brand', 'pattern', 'year', 'category', 'price', 'owner',)
    list_filter = ['category']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Pattern, PatternAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Car, CarAdmin)