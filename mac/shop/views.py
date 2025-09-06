from collections import defaultdict

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil

# Homepage
def home(request):
    products = Product.objects.all()
    categories = Product.objects.values_list('category', flat=True).distinct()

    products_and_categories = []
    for category in categories:
        products_and_categories.append({
            'category': category,
            'products': products.filter(category=category).order_by('-price'),
        })

    params = {
        'products' : products,
        'products_and_categories' : products_and_categories
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
