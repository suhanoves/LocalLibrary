"""
project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='catalog:home', permanent=True)),
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
