from django.contrib import admin
from .models import Product, WomenProduct, NewArrivalsProduct
# Register your models here.

admin.site.register(Product)
admin.site.register(WomenProduct)
admin.site.register(NewArrivalsProduct)