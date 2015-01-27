# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from mycatalog.catalog.models import Goods


def archive(request):
    products = Goods.objects.all()
    t = loader.get_template("goods_list.html")
    c = Context({'products': products})
    return HttpResponse(t.render(c))


