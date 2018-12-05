# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
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

class Car(models.Model):
    class Meta():
        ordering = ['-brand', 'pattern', '-year', '-price']
        db_table = 'car'
        verbose_name_plural = 'Cars'
        verbose_name = 'Car'

    brand = models.ForeignKey(Brand, related_name='brand', related_query_name='brand', verbose_name=u'Car brand')
    pattern = models.ForeignKey(Pattern, related_name='pattern', related_query_name='pattern', verbose_name=u'Cur model')
    year = models.IntegerField(verbose_name=u'Graduation year')
    price = models.IntegerField(verbose_name='Car price')
    owner = models.CharField(max_length=50, verbose_name='Owner car')

    def __str__(self):
        return self.owner
