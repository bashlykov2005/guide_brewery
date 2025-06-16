"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap

from django.views.defaults import permission_denied
from axes.decorators import axes_dispatch

from core.sitemaps import StaticViewSitemap, RouteSitemap, BrewerySitemap

sitemaps = {
    "static": StaticViewSitemap,
    "routes": RouteSitemap,
    "breweries": BrewerySitemap,
}

urlpatterns = [
    path("secret-admin-url/", admin.site.urls),  # Смена стандартного /admin/
    path("admin/", lambda r: permission_denied(r, exception=None)),
    path("secret-admin-url/", axes_dispatch(admin.site.urls)),
    # path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    path("", include("main.urls", namespace="main")),
    path("route/", include("route.urls", namespace="route")),
    path("brewery/", include("brewery.urls", namespace="brewery")),
    path("country/", include("country.urls", namespace="country")),
    path("feedback/", include("feedback.urls", namespace="feedback")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),  # для индексации в Яндексе и Google.
]

# Только для разработки (DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
