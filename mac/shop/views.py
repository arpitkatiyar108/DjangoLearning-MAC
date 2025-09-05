from django.http import HttpResponse
from django.shortcuts import render


# Homepage
def home(request):
    return render(request, 'shop\home.html')

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
