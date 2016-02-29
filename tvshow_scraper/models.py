# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from dynamic_scraper.models import Scraper, SchedulerRuntime
from scrapy.contrib.djangoitem import DjangoItem
from leancloud import Object

class Person(models.Model):
    
    name = models.CharField(max_length=200)

    douban_id = models.IntegerField()

    def __unicode__(self):
        return self.name


class Type(models.Model):
    
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=200)

    description = models.TextField(null=True)

    url = models.URLField()

    scraper = models.ForeignKey(Scraper, blank=True, null=True, on_delete=models.SET_NULL)

    scraper_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class TVShow(models.Model):

    name = models.CharField(max_length=200)

    douban_cover = models.ImageField(blank=True,null=True,max_length=200)

    douban_id = models.IntegerField()

    douban_url = models.CharField(max_length=200, null=True)

    douban_rating = models.FloatField()

    director = models.ForeignKey(Person, null=True, blank=True, related_name='%(class)s_director')

    starring = models.ForeignKey(Person, null=True, blank=True, related_name='%(class)s_starring')

    release_at = models.DateTimeField(blank=True,null=True)

    episodes_num = models.IntegerField(blank=True,null=True)

    season_num = models.IntegerField(blank=True,null=True)

    area = models.CharField(max_length=50,null=True)

    summary = models.TextField(null=True)


    types = models.ForeignKey(Type, null=True, blank=True)

    source = models.ForeignKey(Source)

    checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)

    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super(TVShow, self).save(*args, **kwargs)

class TVShowItem(DjangoItem):
    django_model = TVShow

