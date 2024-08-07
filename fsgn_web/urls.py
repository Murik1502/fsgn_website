from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fsgn.urls')),
    path('sgn1/', include('sgn1.urls')),
    path('sgn2/', include('sgn2.urls')),
    path('sgn3/', include('sgn3.urls')),
    path('sgn4/', include('sgn4.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
