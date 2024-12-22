from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.utils.safestring import mark_safe
from django.template import Template, Context


from route.models import Route


def route_index(request, route_slug):

    route = Route.objects.get(slug=route_slug)

    context = {
        "title": "Маршрут",
        'route': route,
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
