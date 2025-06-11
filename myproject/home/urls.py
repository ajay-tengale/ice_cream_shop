

from django.contrib import admin
from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.index, name='home'),           # Homepage
    path('about/', views.about, name='about'),    # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),     # Contact page
    path('cart/', views.cart, name='cart'),       # Cart page
    path('flavors/', views.flavor_view, name='flavors'),
    # path('add-to-cart/<int:flavor_id>/', views.add_to_cart, name='add_to_cart'),
     
]


