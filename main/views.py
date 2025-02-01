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
    breweries = Brewery.objects.all()
    countries = Сountry.objects.all()

    route_dark = range(1, 6)
    route_light = range(6, 62)
    route_disabled = range(62, 100)
    route_20 = range(1, 21)

    paginator = Paginator(routes, 20)
    current_page = paginator.page(int(page))

    paginator = Paginator(breweries, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Главная",
        "routes": current_page,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
        "route_20": route_20,
        "breweries": breweries,
        "page_obj": page_obj,
        "countries": countries,
        # "country": country,
    }
    return render(request, "main/index.html", context=context)


def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context=context)
