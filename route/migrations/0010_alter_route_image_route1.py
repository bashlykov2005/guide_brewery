# Generated by Django 4.2.16 on 2024-12-10 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0009_alter_route_image_route1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='image_route1',
            field=models.ImageField(blank=True, null=True, upload_to='media/route_images/route'),
        ),
    ]
