from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^infolab/', include('infolab.foo.urls')),

    (r'^people/(?P<uname>\w+)$', 'people.views.detail'),
    (r'^people/(?P<uname>\w+)/?$', 'people.views.detail'),
    (r'^people/?$', 'people.views.index'),

    (r'^pub', 'people.views.publist'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^admin/(.*)', admin.site.root),

    (r'^$', 'web.views.index'), # answers for everything

    url(r'^', include('basic.blog.urls')), # answers for everything
)
