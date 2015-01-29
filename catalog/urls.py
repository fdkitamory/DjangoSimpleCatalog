from django.conf.urls.defaults import *
from mycatalog.catalog.views import index, categories

urlpatterns = patterns('mycatalog.catalog.views',
    url(r'^$', index),
    url(r'^(?P<category_name>\w+)/$', categories),
    url(r'^category/$', categories),
)