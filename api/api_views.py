
from fitness_project.core.nutrition.models import NutritionLog
from fitness_project.core.workouts.models import Workout
from rest_framework import viewsets, permissions
from fitness_project.core.nutrition.serializers import NutritionLogSerializer
from fitness_project.core.workouts.serializers import WorkoutSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class NutritionLogViewSet(viewsets.ModelViewSet):
    queryset = NutritionLog.objects.all()
    serializer_class = NutritionLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

from rest_framework import viewsets
from fitness_project.core.workouts.models import Achievement
from fitness_project.core.workouts.serializers import AchievementSerializer

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

# Placeholder: JWT Authentication & Pagination Setup
from rest_framework.authentication import BaseAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from fitness_project.core.workouts.models import Achievement
from fitness_project.core.workouts.serializers import AchievementSerializer
from rest_framework import viewsets

# Simple pagination logic
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Placeholder JWT Authentication class
class CustomJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Simulated JWT logic (mock, no real validation)
        return (request.user, None)

class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
