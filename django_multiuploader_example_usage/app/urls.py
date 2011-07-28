from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'app.views.image_view', name='main'),
)