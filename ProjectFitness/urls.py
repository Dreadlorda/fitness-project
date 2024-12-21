from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import include, path

from users.views import about_us, contact_us
from .views import home, index  # Import the home view from the views.py file

urlpatterns = [
    path('', lambda request: redirect('index')),
    path('index/', index, name='index'),
    path('admin/', admin.site.urls),
    path('workouts/', include('workouts.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('users/', include('users.urls')),
    path('goals/', include('goals.urls')),
    path('about/', about_us, name='about-us'),
    path('contact/', contact_us, name='contact-us'),
    path('', home, name='home'),  # Use the home view for the root URL
    path('api/', include('async_rest_integration.urls')),  # Added async API routes
]

def custom_403_view(request, exception):
    return render(request, '403.html', status=403)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

handler403 = custom_403_view
handler404 = custom_404_view
handler500 = custom_500_view

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)