__author__ = 'frank'


def breadcrumbs(request):
    return {
        'breadcrumbs': request.path.split('/')
    }