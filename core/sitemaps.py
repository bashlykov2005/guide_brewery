from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from brewery.models import Brewery
from route.models import Route


# Статические страницы (без параметров)
class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return ["main:index"]  # Только главная

    def location(self, item):
        return reverse(item)


# Для маршрутов (Route)
class RouteSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        routes = Route.objects.all()
        # Возвращаем не только объекты, но и типы страниц
        return (
            [(route, "index") for route in routes]
            + [(route, "descr") for route in routes]
            + [(route, "city") for route in routes]
        )

    def location(self, item):
        route, page_type = item
        if page_type == "index":
            return reverse("route:route_index", kwargs={"route_slug": route.slug})
        elif page_type == "descr":
            return reverse("route:route_descr", kwargs={"route_slug": route.slug})
        elif page_type == "city":
            return reverse("route:route_city", kwargs={"route_slug": route.slug})


# Для пивоварен (Brewery)
class BrewerySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Brewery.objects.all()

    def location(self, item):
        return reverse("brewery:brewery_index", kwargs={"brewery_slug": item.slug})
