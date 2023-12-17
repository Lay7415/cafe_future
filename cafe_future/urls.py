from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/access_management/', include('access_management.urls')),
    path('client/food/', include('food.urls')),
    path('client/tables/', include('tables.urls')),
    path('', include('main.urls')),
    # path('', include('food_news.urls')),
    path('client/basket/', include('basket.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
