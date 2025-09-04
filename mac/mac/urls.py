from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),   # URLs from shop app mounted at /shop/
    path('blog/', include('blog.urls')),   # URLs from blog app mounted at /blog/
    path('', include('shop.urls')),        # optional: make shop the site root (or map home view directly)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)