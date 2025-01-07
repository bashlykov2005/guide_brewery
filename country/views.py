from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

from route.models import Route
from country.models import Сountry
from brewery.models import Brewery


def country_routes(request, country_slug):

    routes = Route.objects.all()
    # breweries = Brewery.objects.all()
    country = Сountry.objects.get(slug=country_slug)

    route_dark = range(1, 6)
    route_light = range(6, 59)
    route_disabled = range(59, 100)
    route_20 = range(1, 21)

    paginator = Paginator(routes, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Маршруты",
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
        "route_20": route_20,
        # "breweries": breweries,
        "country": country,
        "routes": country.routes.all(),
        "page_obj": page_obj,
    }
    return render(request, "country/country-route.html", context=context)


# def country_route(request, country_slug, route_slug):
#     route = get_object_or_404(Route, slug=route_slug)
#     return render(
#         request,
#         "route.html",
#         {
#             "route": route,
#             "breweries": route.brewery_set.all(),
#         },
#     )

# def country_route_breweries(request, country_slug, route_slug):
#     route = get_object_or_404(Route, slug=route_slug)
#     return render(
#         request,
#         "route_breweries.html",
#         {
#             "route": route,
#             "breweries": route.brewery_set.all(),
#         },
#     )

# def country_route_brewery(request, country_slug, route_slug, brewery_slug):
#     route = get_object_or_404(Route, slug=route_slug)
#     country = get_object_or_404(Сountry, slug=country_slug)
#     brewery = get_object_or_404(Brewery, slug=brewery_slug)
#     return render(
#         request,
#         "route_brewery.html",
#         {
#             "route": route,
#             "brewery": brewery,
#             "breweries": route.brewery_set.all(),
#         },
#     )
