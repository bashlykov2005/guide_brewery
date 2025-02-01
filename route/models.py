import uuid
from django.db import models
from django.urls import reverse


def uuid_url():
    return uuid.uuid4()


class Route(models.Model):
    class Meta:
        db_table = "routes"
        verbose_name = "Маршруты"
        verbose_name_plural = "Маршруты"
        ordering = ("id",)

    name = models.CharField(
        verbose_name="Название маршрута",
        max_length=100,
        unique=True,
        error_messages={"unique": "такой маршрут уже существует"},
    )
    slug = models.SlugField(
        max_length=110, verbose_name="URL", unique=True, blank=True, null=True
    )
    base_city = models.CharField(max_length=50, verbose_name="Базовый город")
    base_city_2 = models.CharField(
        max_length=50, verbose_name="Базовый город 2", blank=True, null=True
    )
    city_slug = models.SlugField(
        max_length=110, verbose_name="URL_city", blank=True, null=True
    )
    base_city_3 = models.CharField(
        max_length=50, verbose_name="Базовый город 3", blank=True, null=True
    )
    city_desc = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name="Описание города"
    )
    city_desc_2 = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name="Описание города 2"
    )
    route_desc = models.TextField(
        max_length=7000, blank=True, null=True, verbose_name="Описание маршрута"
    )
    link = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="Ссылка при наведении"
    )
    image_route1 = models.ImageField(
        upload_to="route_images/route",
        blank=True,
        null=True,
    )
    image_route2 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route3 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route4 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route5 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route6 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route7 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route8 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route9 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route10 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route11 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route12 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route13 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_route14 = models.ImageField(
        upload_to="route_images/route", blank=True, null=True, default="100.jpeg"
    )
    image_city1 = models.ImageField(
        upload_to="route_images/city",
        blank=True,
        null=True,
        default="route_images/city/100.jpeg",
    )
    image_city2 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city3 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city4 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city5 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city6 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city7 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city8 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city9 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city10 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city11 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    image_city12 = models.ImageField(
        upload_to="route_images/city", blank=True, null=True, default="100.jpeg"
    )
    def get_absolute_url(self):
        return reverse("route", kwargs={"route_slug": self.slug})

    def __repr__(self):
        return f"<{self.name}>"

    def __str__(self):
        return f"{self.name}"
