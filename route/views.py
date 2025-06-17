from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context


from brewery.models import Brewery
from route.models import Route


def route_index(request, route_slug):

    routes = Route.objects.all()
    route = Route.objects.get(slug=route_slug)

    # Сохраняем slug текущего маршрута в сессии
    request.session["last_route_slug"] = route_slug

    route_dark = range(1, 6)
    route_light = range(6, 70)
    route_disabled = range(70, 100)

    context = {
        "title": "Маршрут",
        "routes": routes,
        "route": route,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
    }
    return render(request, "route/route.html", context=context)


def route_index_search(request, route_slug):

    routes = Route.objects.all()

    route = Route.objects.get(slug=route_slug)

    route_dark = range(1, 6)
    route_light = range(6, 70)
    route_disabled = range(70, 100)

    context = {
        "title": "Маршрут",
        "routes": routes,
        "route": route,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
    }
    return render(request, "route/route_2.html", context=context)


def route_descr(request, route_slug):
    route = Route.objects.get(slug=route_slug)
    breweries = route.brewery_set.all()  #  связанные пивоварни

    # Создаём шаблон из строки в БД и рендерим его с контекстом
    template_from_db = Template(route.route_desc)
    rendered_description = template_from_db.render(
        Context(
            {
                "route": route,
                "breweries": breweries,
            }
        )
    )

    context = {
        "title": "Описание маршрута",
        "route": route,
        "breweries": breweries,
        "rendered_description": rendered_description,  # Передаём обработанный HTML в наш route-description.html
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


def brewery_index(request, brewery_slug):

    brewery = Brewery.objects.get(slug=brewery_slug)

    context = {
        "title": "Пивоварня",
        "brewery": brewery,
    }
    return render(request, "brewery/brewery.html", context=context)
