# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone
from datetime import datetime


class Brand(models.Model):
    class Meta():
        db_table = 'brand'
        verbose_name_plural = 'Brands'
        verbose_name = 'Brand'

    name = models.CharField(max_length=50, unique=True, verbose_name='Brand')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Pattern(models.Model):
    class Meta():
        db_table = 'pattern'
        verbose_name_plural = 'Patterns'
        verbose_name = 'Pattern'

    name = models.CharField(max_length=50, unique=True, verbose_name='Pattern')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = 'Categorys'
        verbose_name = 'Category'
        ordering = ['-name']

    name = models.CharField(max_length=150, verbose_name='Category')
    parent = TreeForeignKey('self',  on_delete=models.CASCADE,  null=True, blank=True, related_name='children',
                            verbose_name=u'Parent class')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Car(models.Model):
    class Meta():
        ordering = ['-brand', 'pattern', '-year', '-price']
        db_table = 'car'
        verbose_name_plural = 'Cars'
        verbose_name = 'Car'

    brand = models.ForeignKey(Brand, related_name='brand', related_query_name='brand', verbose_name=u'Car brand')
    pattern = models.ForeignKey(Pattern, related_name='pattern', related_query_name='pattern', verbose_name=u'Cur model')
    year = models.IntegerField(verbose_name=u'Graduation year')
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')
    price = models.IntegerField(verbose_name='Car price')
    owner = models.CharField(max_length=50, verbose_name='Owner car')

    def __str__(self):
        return self.owner

    def addcategory(self, year, category):
        for y in year:
            if y < 1990:
                category == 'Until 1990 release'
            elif 1990 <= y < 2000:
                category == 'From 1990 to 2000, the release'
            elif 2000 <= y < 2010:
                category == 'From 2000 to 2010 release'
            elif y >= 2010:
                category == 'After 2010 release'
            else:
                print 'No category'
        return category