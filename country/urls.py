from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from country import views

app_name = "country"

urlpatterns = [
    path("<slug:country_slug>/", views.country_routes, name="country_routes"),
    # path("<slug:route_slug>/route_descr/", views.route_descr, name="route_descr"),
    # path("<slug:route_slug>/route_city/", views.route_city, name="route_city"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
