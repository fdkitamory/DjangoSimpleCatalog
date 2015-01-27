from django.conf.urls.defaults import *
from mycatalog.catalog.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)