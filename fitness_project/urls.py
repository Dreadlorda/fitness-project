
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('workouts/', include('fitness_project.core.workouts.urls')),
    path('goals/', include('fitness_project.core.goals.urls')),
    path('nutrition/', include('fitness_project.core.nutrition.urls')),
    path('admin/', admin.site.urls),
    path('fitness_project.core.workouts/', include('fitness_project.core.workouts.urls')),  # Updated to include the w...
    path('', include('users.urls')),  # Existing user routes
    path('', include('fitness_project.core.nutrition.urls')),  # Existing fitness_project.core.nutrition routes

    path('accounts/', include('allauth.urls')),
]

