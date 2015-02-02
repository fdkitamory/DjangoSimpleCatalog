__author__ = 'frank'


def breadcrumb_processor(request):
    return {
        'breadcrumbs': request.path.split('/')
    }