# shop/urls.py
from django.urls import path
from . import views  # Import views from this app

urlpatterns = [
    path('', views.home, name='shop_home'),
    path('about/', views.about, name='shop_about'),
    path('contact/', views.contact, name='shop_contact'),
    path('tracker/', views.order_tracker, name='shop_tracker'),
    path('search/', views.search_products, name='shop_search'),
    path('product/<int:id>/', views.product_detail, name='shop_product_detail'),
    path('checkout/', views.checkout, name='shop_checkout'),
]
