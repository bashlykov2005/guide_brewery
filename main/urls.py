from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from main import views
from .views import (FeedbackCreateView)

app_name = 'main'


urlpatterns = [
    path("search/", views.index, name="search"),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("write/", FeedbackCreateView.as_view(), name="feedbackcreateview"),
    path("massage/", views.feedback_massage, name="feedback_massage"),
    path("admin-prelogin/", views.admin_prelogin, name="admin_prelogin"),
    path("admin-redirect/", views.protected_admin_redirect, name="admin_redirect"),
    path("oferta/", views.oferta_view, name="oferta"),
    path("privacy/", views.privacy_view, name="privacy"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
