from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),

    path('api/v1/auth/', include('authentication.urls')),
    path('api/v1/vendor/', include('vendor.urls')),
    path('api/v1/market/', include('market.urls')),
    path('api/v1/order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)