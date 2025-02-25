from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


from brewery.models import Brewery
from route.models import Route


def route_index(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    route_dark = range(1, 6)
    route_light = range(6, 70)
    route_disabled = range(70, 100)

    context = {
        "title": "Маршрут",
        "route": route,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
    }
    return render(request, "route/route.html", context=context)


def route_descr(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    # Template("{{ route.route_desc }}").render(
    # Context({"route.route_desc": mark_safe('<img src="{{ route.image_route1.url }}" width="300" height="200" alt="Иллюстрация" class="leftfoto">')})
    # )
    context = {
        "title": "Описание маршрута",
        "route": route,
        "breweries": route.brewery_set.all(),
        # "route.route_desc": mark_safe('<img src="{{ route.image_route1.url }}" width="300" height="200" alt="Иллюстрация" class="leftfoto">')
    }
    return render(request, "route/route-description.html", context=context)


def route_city(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Базовый город",
        "route": route,
    }
    return render(request, "route/route-base-city.html", context=context)


def route_city_2(request, route_slug, route_base_city):

    route = Route.objects.get(slug=route_slug)
    # route_base_city =route.base_city

    context = {
        "title": "Второй базовый город",
        "route": route,
    }
    return render(request, "route/route-base-city_2.html", context=context)


def route_breweries(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Пивоварни на маршруте",
        "route": route,
        "breweries": route.brewery_set.all(),
    }
    return render(request, "route/route-breweries.html", context=context)


def route_brewery(request, route_slug, brewery_slug):

    route = Route.objects.get(slug=route_slug)
    brewery = Brewery.objects.get(slug=brewery_slug)

    context = {
        "title": "Пивоварня",
        "route": route,
        "brewery": brewery,
        # "breweries": route.brewery_set.all(),
    }
    return render(request, "route/route-brewery.html", context=context)


def route_descr_brewery(request, route_slug, brewery_slug):

    route = Route.objects.get(slug=route_slug)
    brewery = Brewery.objects.get(slug=brewery_slug)

    context = {
        "title": "Пивоварня",
        "route": route,
        "brewery": brewery,
        # "breweries": route.brewery_set.all(),
    }
    return render(request, "route/route-descr-brewery.html", context=context)
