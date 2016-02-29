from dynamic_scraper.spiders.django_spider import DjangoSpider
from tvshow_scraper.models import Source, TVShow, TVShowItem
import django
django.setup()

class TVShowSpider(DjangoSpider):
    
    name = 'tvshow_spider'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(Source, **kwargs)
        self.scraper = self.ref_object.scraper
        self.scrape_url = self.ref_object.url
        self.scheduler_runtime = self.ref_object.scraper_runtime
        self.scraped_obj_class = TVShow
        self.scraped_obj_item_class = TVShowItem
        super(TVShowSpider, self).__init__(self, *args, **kwargs)