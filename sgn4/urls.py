from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('applicant/', views.Applicant.as_view(), name='applicant-sgn4')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
