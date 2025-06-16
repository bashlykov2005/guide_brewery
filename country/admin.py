from django.contrib import admin

from country.models import Сountry

class СountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "slug",
        "link",
    )
    list_display_links = ("id",)
    search_fields = ("name",)
    list_editable = (
        "name",
        "slug",
        "link",
    )
    list_filter = ("name",)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Сountry, СountryAdmin)
