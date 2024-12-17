
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workouts/', include('workouts.urls')),  # Updated to include the w...
    path('', include('users.urls')),  # Existing user routes
    path('', include('nutrition.urls')),  # Existing nutrition routes
]

path('accounts/', include('allauth.urls')),
