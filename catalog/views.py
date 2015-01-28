# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
import mycatalog.catalog.models


def index(request):
    items = mycatalog.catalog.models.Item.objects.all()
    t = loader.get_template("goods_list.html")
    c = Context({'items': items})
    return HttpResponse(t.render(c))


