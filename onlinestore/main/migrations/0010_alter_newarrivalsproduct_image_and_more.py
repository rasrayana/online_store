# Generated by Django 5.0.3 on 2024-03-25 19:03

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_newarrivalsproducts_newarrivalsproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newarrivalsproduct',
            name='image',
            field=models.ImageField(upload_to=main.models.new_arrival_product_image_upload_to, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='womenproduct',
            name='image',
            field=models.ImageField(upload_to=main.models.women_product_image_upload_to, verbose_name='Изображение'),
        ),
    ]