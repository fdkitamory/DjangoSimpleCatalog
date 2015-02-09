__author__ = 'frank'

from django.core.paginator import Paginator, EmptyPage


def page_pagination(request, paginate_items, number_of_pages):
    paginator = Paginator(paginate_items, number_of_pages)
    page = request.GET.get('page', '1')
    page = int(page)

    try:
        paginate_items = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        paginate_items = paginator.page(paginator.num_pages)

    return paginate_items