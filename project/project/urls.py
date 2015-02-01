from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'shortener.views.index', name='home'),
    url(r'^shorten', 'shortener.views.shorten', name='shorten'),
    url(r'^get/([\w]+)', 'shortener.views.getURL', name='getURL'),
)
