from django.db import models
from django.urls import reverse
from django.core.paginator import Paginator

from country.models import Сountry
from route.models import Route

class Brewery(models.Model):

    """Модель для создания пивоварен"""

    class Meta:
        db_table = "breweries"
        verbose_name = "Пивоварни"
        verbose_name_plural = "Пивоварни"
        ordering = ["id"]

    title = models.CharField(
        verbose_name="Название пивоварни",
        max_length=100,
        unique=True,
    )
    slug = models.SlugField(
        max_length=100, verbose_name="URL", unique=True, blank=True, null=True
    )
    address = models.CharField(
        max_length=150,
        verbose_name="Адресс",
        blank=True,
        null=True,
    )
    map_link = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Ссылка на карту",
        null=True,
    )
    working_hours = models.CharField(
        max_length=100,
        verbose_name="Часы работы",
        blank=True,
        null=True,
    )
    sait_link = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="сайт",
        null=True,
    )
    link = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Ссылка при наведении"
    )
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Описание пивоварни"
    )
    descript_full = models.TextField(
        max_length=5000, blank=True, null=True, verbose_name="Описание пивоварни полное"
    )
    image1 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image2 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image3 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image4 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image5 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image6 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image7 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image8 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image9 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    image10 = models.ImageField(
        upload_to="brewery_images", blank=True, null=True, default="100.jpeg"
    )
    route_id = models.ForeignKey(
        to=Route,
        on_delete=models.PROTECT,
        verbose_name="Категория-маршрут",
    )
    country_id = models.ForeignKey(
        to=Сountry,
        on_delete=models.PROTECT,
        default=1,
        verbose_name="Категория-страна",
    )

    def get_absolute_url(self):
        return reverse("brewery", kwargs={"brewery_slug": self.slug})

    def __repr__(self):
        return f"<Пивоварня: {self.title}>"

    def __str__(self):
        return f"Пивоварня: {self.title}"


# Create your models here.
