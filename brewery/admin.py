from django.contrib import admin

from brewery.models import Brewery

class BreweryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "address",
        "working_hours",
        "map_link",
        "sait_link",
        "link",
        "description",
        "image1",
        "image2",
        "image3",
        "image4",
        "image5",
        "image6",
        "route_id",
        "country_id",
    )
    list_display_links = ("id",)
    search_fields = ("title",)
    list_editable = (
        "title",
        "slug",
        "address",
        "working_hours",
        "map_link",
        "sait_link",
        "link",
        "description",
        "image1",
        "image2",
        "image3",
        "image4",
        "image5",
        "image6",
        "route_id",
        "country_id",
    )
    list_filter = ("title",)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Brewery, BreweryAdmin)
