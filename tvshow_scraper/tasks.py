from celery.task import task
from django.db.models import Q
from dynamic_scraper.utils.task_utils import TaskUtils
from tvshow_scraper.models import TVShow, Source

@task()
def run_spiders():
    t = TaskUtils()
    #Optional: Django field lookup keyword arguments to specify which reference objects (NewsWebsite)
    #to use for spider runs, e.g.:
    kwargs = {}
    #Optional as well: For more complex lookups you can pass Q objects vi args argument
    args = ()
    t.run_spiders(Source, 'scraper', 'scraper_runtime', 'tvshow_spider', *args, **kwargs)

# @task()
# def run_checkers():
#     t = TaskUtils()
#     #Optional: Django field lookup keyword arguments to specify which reference objects (Article)
#     #to use for checker runs, e.g.:
#     kwargs = {
#         'check_me': True, #imaginary, model Article hat no attribute 'check_me' in example
#     }
#     #Optional as well: For more complex lookups you can pass Q objects vi args argument
#     args = (Q(id__gt=100),)
#     t.run_checkers(Article, 'news_website__scraper', 'checker_runtime', 'article_checker', *args, **kwargs)