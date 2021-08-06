"""
project URL Configuration
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from project import settings

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='catalog:index', permanent=True)),
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]

# Serving static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serving files uploaded by a user during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Add Django authentication views
urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]
