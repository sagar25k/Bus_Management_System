from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from .views import index, buses, drivers, routes, incharges, staff, students, addbus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('buses/', include('buses.urls')),
    path('drivers/', include('drivers.urls')),
    path('routes/', include('routes.urls')),
    path('incharges/', include('incharges.urls')),
    path('staff/', include('staff.urls')),
    path('students/', include('students.urls')),
    path('registrations/', include('registrations.urls')),  # Include registrations app URLs
    path('accounts/', include('django.contrib.auth.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    re_path(r'^.*$', index, name='index'),  # Catch-all pattern for fallback
]

# Static and media file configurations
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
