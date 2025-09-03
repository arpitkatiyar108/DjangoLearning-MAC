from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),   # URLs from shop app mounted at /shop/
    path('blog/', include('blog.urls')),   # URLs from blog app mounted at /blog/
    path('', include('shop.urls')),        # optional: make shop the site root (or map home view directly)
]
