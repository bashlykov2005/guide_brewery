from django import template
from django.utils.http import urlencode

from route.models import Route

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Route.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context["request"].GET.dict()
    query.update(kwargs)
    return urlencode(query)


@register.filter(name="is_instance")
def is_instance(value, class_name):
    return value.__class__.__name__ == class_name
