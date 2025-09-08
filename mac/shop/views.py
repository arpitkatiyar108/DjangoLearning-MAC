from collections import defaultdict

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    return render(request, 'shop\contact.html')

# Order Tracker Page
def order_tracker(request):
    return render(request, 'shop\\tracker.html')

# Search Products Page
def search_products(request):
    return render(request, 'shop\search.html')

# Product Detail Page
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'shop\product_view.html', {'product': product})

# Checkout Page
def checkout(request):
    return render(request, 'shop\checkout.html')
