from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('securelogin/', admin.site.urls),
    path('', include('app.home.urls')),
    path('accounts/', include('app.accounts.urls')),
    path('store/', include('app.store.urls')),
    path('cart/', include('app.carts.urls')),
    path('orders/', include('app.orders.urls')),
    path('', include('app.payments.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
