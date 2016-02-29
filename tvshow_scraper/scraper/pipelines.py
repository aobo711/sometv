# -*- coding: utf-8 -*-
from django.db.utils import IntegrityError
from scrapy import log
import time
from scrapy.exceptions import DropItem
from dynamic_scraper.models import SchedulerRuntime
from tvshow_scraper.models import TVShow
from django.forms.models import model_to_dict

from leancloud import Object, Query



def item_to_model(item):
    model_class = getattr(item, 'django_model')
    if not model_class:
        raise TypeError("Item is not a `DjangoItem` or is misconfigured")

    return item.instance


def get_or_create(model):
    model_class = type(model)
    created = False

    # Normally, we would use `get_or_create`. However, `get_or_create` would
    # match all properties of an object (i.e. create a new object
    # anytime it changed) rather than update an existing object.
    #
    # Instead, we do the two steps separately
    try:
        # We have no unique identifier at the moment; use the name for now.
        obj = model_class.objects.get(douban_id=model.douban_id)
        obj['updated_at'] = time.strftime("%c")
    except model_class.DoesNotExist:
        created = True
        obj = model  # DjangoItem created a model for us.

    return (obj, created)


def update_model(destination, source, commit=True):
    pk = destination.pk

    source_dict = source.__dict__
    for (key, value) in source_dict.items():
        setattr(destination, key, value)

    setattr(destination, 'pk', pk)

    if commit:
        destination.save()
        

    return destination


class DjangoWriterPipeline(object):

    def process_item(self, item, spider):
        try:

            checker_rt = SchedulerRuntime(runtime_type='C')
            checker_rt.save()
            item['checker_runtime'] = checker_rt
            item['source'] = spider.ref_object

            try:
                item_model = item_to_model(item)
            except TypeError:
                return item
            
            model, created = get_or_create(item_model)
            
            update_model(model, item_model)
            
            if created:
                spider.log('==' + model.name + '== created.', log.INFO)
            else:
                spider.log('==' + model.name + '== updated.', log.INFO)

            spider.action_successful = True

        except IntegrityError, e:
            spider.log(str(e), log.ERROR)
            raise DropItem("Missing attribute.")

        return item


