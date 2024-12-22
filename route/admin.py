from django.contrib import admin
from django.utils.safestring import mark_safe

from route.models import Route

class RouteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "base_city",
        # "base_city_2",
        # "base_city_3",
        # "city_desc",
        # "city_desc_2",
        "route_desc",
        # "link",
        "image_route1",
        # "image_route2",
        # "image_route3",
        # "image_route4",
        # "image_route5",
        # "image_route6",
        "image_city1",
        "image_city2",
        "image_city3",
        "image_city4",
        "image_city5",
        "image_city6",
        "image_city7",
        "image_city8",
        "image_city9",
        "image_city10",
        "image_city11",
        "image_city12",
    )
    list_display_links = ('id',)
    search_fields = ("name", 'base_city')
    list_editable = (
        "name",
        "slug",
        "base_city",
        # "base_city_2",
        # "base_city_3",
        # "city_desc",
        # "city_desc_2",
        # "base_city_3",
        "route_desc",
        # "link",
        "image_route1",
        # "image_route2",
        # "image_route3",
        # "image_route4",
        # "image_route5",
        # "image_route6",
        "image_city1",
        "image_city2",
        "image_city3",
        "image_city4",
        "image_city5",
        "image_city6",
        "image_city7",
        "image_city8",
        "image_city9",
        "image_city10",
        "image_city11",
        "image_city12",
    )
    list_filter = ("name", "base_city",)
    prepopulated_fields = {"slug": ("name",)}
    save_on_top = True

admin.site.register(Route, RouteAdmin)


@admin.display(description="Изображение")
def post_photo1(self, route: Route):
    return mark_safe(f'<img src="{route.image_route1.url}" width="300" height="200" alt="Иллюстрация" class="leftfoto">')
