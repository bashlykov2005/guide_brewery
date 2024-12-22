from django.db import models
from django.urls import reverse

from route.models import Route

class Сountry(models.Model):
    class Meta:
        db_table = "countries"
        verbose_name = "Страны"
        verbose_name_plural = "Страны"
        ordering = ["id"]

    name = models.CharField(verbose_name="Наименование", max_length=50, unique=True)
    slug = models.SlugField(
        max_length=50, verbose_name="URL", unique=True, blank=True, null=True
    )
    link = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="Ссылка при наведении"
    )
    routes = models.ManyToManyField(to=Route)

    def get_absolute_url(self):
        return reverse("country", kwargs={"country_slug": self.slug})

    def __repr__(self):
        return self.name

    def __str__(self):
        return f"{self.name}"
