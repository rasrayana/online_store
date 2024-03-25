from django.db import models
from django.utils import timezone

# Create your models here.

def product_image_upload_to(instance, filename):
    return f'men_products/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
class Product(models.Model):
    title = models.CharField('Название',max_length=100)
    image = models.ImageField('Изображение',upload_to='product_images/')
    type = models.CharField('Тип',max_length=50)
    price = models.DecimalField('Цена',max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Карта товара Men'
        verbose_name_plural = 'Карты товаров Men'



def women_product_image_upload_to(instance, filename):
    return f'women_products/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
class WomenProduct(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to=women_product_image_upload_to)
    type = models.CharField('Тип', max_length=50)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта товара Women'
        verbose_name_plural = 'Карты товаров Women'




def new_arrival_product_image_upload_to(instance, filename):
    return f'new_arrival_products/{timezone.now().strftime("%Y/%m/%d")}/{filename}'
class NewArrivalsProduct(models.Model):
    title = models.CharField('Название', max_length=100)
    image = models.ImageField('Изображение', upload_to=new_arrival_product_image_upload_to)
    type = models.CharField('Тип', max_length=50)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карта товара New Arrivals'
        verbose_name_plural = 'Карты товаров New Arrivals'