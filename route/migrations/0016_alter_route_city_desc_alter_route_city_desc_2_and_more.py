# Generated by Django 4.2.17 on 2025-04-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0015_route_image_route15_route_image_route16'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='city_desc',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Описание города'),
        ),
        migrations.AlterField(
            model_name='route',
            name='city_desc_2',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Описание города 2'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_desc',
            field=models.TextField(blank=True, max_length=50000, null=True, verbose_name='Описание маршрута'),
        ),
    ]
