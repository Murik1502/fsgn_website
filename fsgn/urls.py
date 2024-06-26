from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Main.as_view()),
    path('history/', views.History.as_view()),
    path('applicant/', views.Applicant.as_view()),
    path('science/', views.Science.as_view()),
    path('postgraduate/', views.Postgraduate.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
