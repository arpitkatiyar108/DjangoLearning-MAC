from django.shortcuts import render

def home(request):
    # Renders 'shop/home.html' -> file should be shop/templates/shop/home.html
    return render(request, 'blog/home.html')
