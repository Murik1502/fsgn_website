from django.urls import path

from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('about/', views.About.as_view(), name='about-sgn2'),
    path('applicant/', views.Applicant.as_view(), name='applicant-sgn2'),
    path('history/', views.History.as_view(), name='history-sgn2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
