from django.conf.urls.defaults import *
from mycatalog.catalog.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)