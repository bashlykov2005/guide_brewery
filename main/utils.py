from typing import Union, List
from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)
from django.db.models import Value

from route.models import Route
from brewery.models import Brewery


def q_search(query) -> List[Union[Route, Brewery]]:
    words = query.lower().split()  # Разбиваем запрос на слова для проверки

    # Поиск по модели Route
    route_vector = SearchVector(
        "name",
        "route_desc",
        "base_city",
        "base_city_2",
        "base_city_3",
        "link",
    )
    route_query = SearchQuery(query)

    route_results = (
        Route.objects.annotate(
            rank=SearchRank(route_vector, route_query), content_type=Value("route")
        )
        .filter(rank__gt=0)
        .order_by("-rank")
        .annotate(
            headline=SearchHeadline(
                "name",
                route_query,
                start_sel='<span style="color: yellow;">',
                stop_sel="</span>",
            )
        )
        .annotate(
            bodyline=SearchHeadline(
                "link",
                route_query,
                start_sel='<span style="color: yellow;">',
                stop_sel="</span>",
            )
        )
    )

    # Поиск по модели Brewery
    brewery_vector = SearchVector(
        "title",
        "address",
        "descript_full",
    )
    brewery_query = SearchQuery(query)

    brewery_results = (
        Brewery.objects.annotate(
            rank=SearchRank(brewery_vector, brewery_query),
            content_type=Value("brewery"),
        )
        .filter(rank__gt=0)
        .order_by("-rank")
        .annotate(
            headline=SearchHeadline(
                "title",
                brewery_query,
                start_sel='<span style="color: yellow;">',
                stop_sel="</span>",
            )
        )
        .annotate(
            bodyline=SearchHeadline(
                "descript_full",
                brewery_query,
                start_sel='<span style="color: yellow;">',
                stop_sel="</span>",
            )
        )
    )

    # Фильтрация: оставляем только записи, где ВСЕ слова из запроса есть в тексте
    def contains_all_words(obj, fields):
        text = " ".join(str(getattr(obj, field, "")) for field in fields).lower()
        return all(word in text for word in words)

    # Применяем фильтрацию только если запрос содержит несколько слов
    if len(words) > 1:
        route_results = [
            r for r in route_results
            if contains_all_words(r, ["name", "route_desc", "base_city", "link"])
        ]
        brewery_results = [
            b for b in brewery_results
            if contains_all_words(b, ["title", "address", "descript_full"])
        ]

    # Объединяем и сортируем результаты
    combined_results = list(route_results) + list(brewery_results)
    combined_results.sort(
        key=lambda x: (
            not hasattr(x, "headline")
            or '<span style="color: yellow;">' not in x.headline,
            -x.rank,
        )
    )
    return combined_results

    # keywords = [word for word in query.split() if len(word) > 2]
    # q_objects = Q()

    # for token in keywords:
    #     q_objects |= Q(name__icontains=token)
    #     q_objects |= Q(route_desc__icontains=token)
    #     q_objects |= Q(city_desc__icontains=token)
    #     q_objects |= Q(city_desc_2__icontains=token)
    #     q_objects |= Q(base_city__icontains=token)
    #     q_objects |= Q(base_city_2__icontains=token)
    #     q_objects |= Q(base_city_3__icontains=token)
    #     q_objects |= Q(link__icontains=token)

    # return Route.objects.filter(q_objects)
