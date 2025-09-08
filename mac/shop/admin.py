from django.contrib import admin
from .models import Product, Contact

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name', 'description', 'category', 'subcategory','price' , 'pub_date','image' )  # Show these columns
    search_fields = ('product_id','product_name', 'description', 'category', 'subcategory','price' , 'pub_date','image')            # Search by product name

admin.site.register(Product, ProductAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('message_id','name', 'email', 'phone', 'desc')  # Show these columns
    search_fields = ('message_id','name', 'email', 'phone', 'desc')            # Search by product name

admin.site.register(Contact, ContactAdmin)
