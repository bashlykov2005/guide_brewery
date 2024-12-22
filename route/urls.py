from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from route import views

app_name = "route"

urlpatterns = [
    path("<slug:route_slug>/", views.route_index, name="route_index"),
    path("<slug:route_slug>/route_descr/", views.route_descr, name="route_descr"),
    path("<slug:route_slug>/route_city/", views.route_city, name="route_city"),
    path(
        "<slug:route_slug>/route_city/<str:route_base_city>",
        views.route_city_2,
        name="route_city_2",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
