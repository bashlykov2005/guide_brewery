from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from brewery import views

app_name = "brewery"

urlpatterns = [
    path("<slug:brewery_slug>/", views.brewery_index, name="brewery_index"),
    # path("<slug:route_slug>/route_descr/", views.route_descr, name="route_descr"),
    # path("<slug:route_slug>/route_city/", views.route_city, name="route_city"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
