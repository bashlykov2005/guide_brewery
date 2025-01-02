from django.http import HttpResponse
from django.shortcuts import render
from django.template import context


from brewery.models import Brewery


def brewery_index(request, brewery_slug):

    brewery = Brewery.objects.get(slug=brewery_slug)

    context = {
        "title": "Пивоварня",
        "brewery": brewery,
    }
    return render(request, "brewery/brewery.html", context=context)
