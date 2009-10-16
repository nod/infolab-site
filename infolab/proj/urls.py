from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^twtop/$', 'proj.views.twtop'),
    (r'^twtop_t/$', 'proj.views.twtop_t'),
    (r'^twtop3/(?P<name>[a-zA-Z0-9_]+)/$', 'proj.views.twtop3'),
    (r'^twchart/(?P<num>\d+)/$', 'proj.views.twchart'),
    (r'^twdata/(?P<num>\d+)/$', 'proj.views.twdata'),
    (r'^twletterdata/(?P<name>[a-zA-Z0-9_]+)/$', 'proj.views.twletterdata'),
)
