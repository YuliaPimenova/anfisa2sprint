from django.shortcuts import render
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description', 'price'
    ).filter(
        is_published__exact=True, is_on_main__exact=True,
        category__is_published=True
    )
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
