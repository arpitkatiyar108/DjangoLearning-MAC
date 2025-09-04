from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'pub_date')  # Show these columns
    search_fields = ('product_name',)            # Search by product name

admin.site.register(Product, ProductAdmin)