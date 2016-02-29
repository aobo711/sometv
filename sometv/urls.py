from django.conf.urls import patterns, include, url
from django.contrib import admin
from sometv import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sometv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^sum/', views.sum),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
