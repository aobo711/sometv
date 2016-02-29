from django.http import HttpResponse,JsonResponse,HttpResponseNotFound,HttpResponseBadRequest
from django.template.loader import render_to_string
from tvshow_scraper.models import TVShow
import dateutil.parser
from django.template import loader, Context
import datetime
from django.db.models import Count

def home(request):
    count = request.GET.get('rating', 8.5)
    date = request.GET.get('date', '20150901')

    try:
        date = dateutil.parser.parse(date)
    except:
        date = datetime.date(2015, 9, 1)

    tvshows = TVShow.objects.exclude(douban_rating__lt=count).exclude(release_at__lt=date)

    tvshows = tvshows.order_by('-release_at', 'douban_rating')

    t = loader.get_template('home.html')
    c = Context({ 'tvshows': tvshows })

    rendered = t.render(c)

    return HttpResponse(rendered, content_type='text/html;charset=utf-8')


def sum(request):

    tvshows = TVShow.objects.order_by('-updated_at')

    t = loader.get_template('sum.html')
    c = Context({ 'tvshows': tvshows })

    rendered = t.render(c)

    return HttpResponse(rendered, content_type='text/html;charset=utf-8')