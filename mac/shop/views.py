from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Homepage
def home(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) - (n // 4))
    params = {
        'products' : products,
        'no_of_slides' : nSlides,
        'range' : range(1, nSlides+1),
        'no_of_purducts': n,
        'no_of_products_per_slide' :  range(1, 4),
    }
    return render(request, 'shop\home.html', params)

# About Us Page
def about(request):
    return render(request, 'shop\\about.html')

# Contact Page
def contact(request):
    return HttpResponse("Contact Us - My Awesome Cart")

# Order Tracker Page
def order_tracker(request):
    return HttpResponse("Track Your Order")

# Search Products Page
def search_products(request):
    return HttpResponse("Search Products Page")

# Product Detail Page
def product_detail(request, id):
    return HttpResponse(f"Product Detail Page for Product ID: {id}")

# Checkout Page
def checkout(request):
    return HttpResponse("Checkout Page")
