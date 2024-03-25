# Generated by Django 5.0.3 on 2024-03-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productw_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WomenProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('image', models.ImageField(upload_to='women_product_images/', verbose_name='Изображение')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Карта товара Women',
                'verbose_name_plural': 'Карты товаров Women',
            },
        ),
        migrations.DeleteModel(
            name='ProductW',
        ),
    ]
