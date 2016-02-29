from django.contrib import admin
from django.conf import settings
from tvshow_scraper.models import TVShow,Source

class TVShowAdmin(admin.ModelAdmin):
    list_display = ('name', 'douban_rating','date_', 'url_')
    list_display_links = ('name',)
    
    ordering = ['-release_at', '-douban_rating']

    def date_(self, instance):
        return instance.release_at.strftime('%Y-%m-%d')

    def url_(self, instance):
        return '<a href="http://movie.douban.com/subject/%s" target="_blank">%s</a>' % (instance.douban_id, instance.douban_id)

    url_.allow_tags = True

class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_', 'scraper')
    list_display_links = ('name',)
    
    def url_(self, instance):
        return '<a href="%s" target="_blank">%s</a>' % (instance.url, instance.url)
    url_.allow_tags = True
    


admin.site.register(TVShow, TVShowAdmin)
admin.site.register(Source, SourceAdmin)