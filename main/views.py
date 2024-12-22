from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from route.models import Route
from country.models import Сountry
from brewery.models import Brewery


def index(request):

    page = request.GET.get('page', 1)

    routes = Route.objects.all()

    route_dark = range(1, 5)
    route_light = range(5, 59)
    route_disabled = range(59, 100)
    route_20 = range(1, 21)

    paginator = Paginator(routes, 20)
    current_page = paginator.page(int(page))

    context = {
        "title": "Главная",
        "routes": current_page,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
        "route_20": route_20,
    }
    return render(request, "main/index.html", context=context)

    # def index(request, page=1):

    #     routes = Route.objects.all()

    #     route_dark = range(1, 5)
    #     route_light = range(5, 54)
    #     route_disabled = range(54, 100)

    #     paginator = Paginator(routes, 20)
    #     current_page = paginator.page(page)

    #     context = {
    #         "title": "Главная",
    #         "routes": current_page,
    #         "route_dark": route_dark,
    #         "route_light": route_light,
    #         "route_disabled": route_disabled,
    #     }
    #     return render(request, "main/index.html", context=context)

def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context=context)
