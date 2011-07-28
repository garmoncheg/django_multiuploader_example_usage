from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # (r'^django_multiuploader/', include('django_multiuploader.urls')),

#    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'', include('multiuploader.urls')),
    url(r'', include('app.urls')),
    
)

from django.conf import settings
from django_multiuploader.settings import MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 
            MEDIA_ROOT,
            'show_indexes': True}),
    )
