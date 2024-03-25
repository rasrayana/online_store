from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('support/', views.support, name='support'),
    path('shoppingbag/', views.shoppingbag, name='shoppingbag'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('contacts/', views.contacts, name='contacts'),
    path('newarrivals/', views.newarrivals, name='newarrivals'),
    path('men/', views.men, name='men'), 
    path('women/', views.women, name='women'),
    path('collections/', views.collections, name='collections'),
    path('myadmin/', admin.site.urls), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
