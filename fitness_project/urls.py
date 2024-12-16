
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workouts.views import WorkoutViewSet
from nutrition.views import NutritionLogViewSet

router = DefaultRouter()
router.register(r'workouts', WorkoutViewSet, basename='workouts')
router.register(r'nutrition', NutritionLogViewSet, basename='nutrition')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('users.urls')),  # Assuming users.urls is set up
]

# Custom error handlers
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'

# URL for the asynchronous demo view
from users.views import AsyncDemoView

urlpatterns += [
    path('async-demo/', AsyncDemoView.as_view(), name='async_demo'),
]

# Custom handler for 403 errors
handler403 = 'django.views.defaults.permission_denied'
