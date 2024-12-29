from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.views.generic import ListView

from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from route.models import Route
from country.models import Сountry
from brewery.models import Brewery


def index(request):

    page = request.GET.get('page', 1)

    routes = Route.objects.all()
    breweries = Brewery.objects.all()
    countries = Сountry.objects.all()

    route_dark = range(1, 6)
    route_light = range(6, 59)
    route_disabled = range(59, 100)
    route_20 = range(1, 21)

    paginator = Paginator(routes, 20)
    current_page = paginator.page(int(page))

    paginator = Paginator(breweries, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "title": "Главная",
        "routes": current_page,
        "route_dark": route_dark,
        "route_light": route_light,
        "route_disabled": route_disabled,
        "route_20": route_20,
        "breweries": breweries,
        "page_obj": page_obj,
        "countries": countries,
    }
    return render(request, "main/index.html", context=context)


# class BreweryListView(ListView):
#     model = Brewery
#     template_name = "main/index.html"
#     paginate_by = 3

#     def get_context_data(self, **kwargs):
#         context = super(BreweryListView, self).get_context_data(**kwargs)
#         breweries = Brewery.objects.all()
#         paginator = Paginator(breweries, self.paginate_by)

#         page = self.request.GET.get("page")

#         try:
#             file_exams = paginator.page(page)
#         except PageNotAnInteger:
#             file_exams = paginator.page(1)
#         except EmptyPage:
#             file_exams = paginator.page(paginator.num_pages)

#         context["breweries"] = file_exams
#         return context


# def index(request, page=1):

#     routes = Route.objects.all()

#     route_dark = range(1, 5)
#     route_light = range(5, 54)
#     route_disabled = range(54, 100)

#     paginator = Paginator(routes, 20)
#     current_page = paginator.page(page)

#     context = {
#         "title": "Главная",
#         "routes": current_page,
#         "route_dark": route_dark,
#         "route_light": route_light,
#         "route_disabled": route_disabled,
#     }
#     return render(request, "main/index.html", context=context)

def about(request):
    context = {
        "title": "Информация",
    }
    return render(request, "main/about.html", context=context)
