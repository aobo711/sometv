from dynamic_scraper.spiders.django_checker import DjangoChecker
from tvshow_scraper.models import TVShow, Source


class TVShowChecker(DjangoChecker):

    name = 'tvshow_checker'

    def __init__(self, *args, **kwargs):
        self._set_ref_object(TVShow, **kwargs)
        self.scraper = self.ref_object.Source.scraper
        #self.scrape_url = self.ref_object.url (Not used any more in DDS v.0.8.3+)
        self.scheduler_runtime = self.ref_object.checker_runtime
        super(TVShowChecker, self).__init__(self, *args, **kwargs)