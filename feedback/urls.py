from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import (FeedbackCreateView,)

app_name = "feedback"

urlpatterns = [
    path("", FeedbackCreateView.as_view(), name="feedbackcreateview"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
