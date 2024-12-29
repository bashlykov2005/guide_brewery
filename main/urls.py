from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path("", views.index, name="index"),
    # path("<int:page>/", views.index, name="index"),
    # path("", views.BreweryListView.as_view(), name="file-exam-view"),
    path("about/", views.about, name="about"),
]
