from django.urls import path
from . import views

app_name = 'shop'     # optional, good for namespacing reverse lookups
urlpatterns = [
    path('', views.home, name='home'),   # /shop/  or / depending how you included it
    # add other shop routes here
]
