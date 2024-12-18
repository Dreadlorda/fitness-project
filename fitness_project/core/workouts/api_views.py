
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.cache import cache

from .models import Goal
from fitness_project.core.nutrition.models import ProgressLog
from fitness_project.core.workouts.models import Workout
from ..goals.serializers import GoalSerializer


class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

@api_view(['GET'])
def analytics_api(request):
    cache_key = f'analytics_{request.user.id}'
    data = cache.get(cache_key)
    if not data:
        total_goals = Goal.objects.filter(user=request.user).count()
        total_workouts = Workout.objects.filter(user=request.user).count()
        total_progress = ProgressLog.objects.filter(user=request.user).count()
        data = {
            'total_goals': total_goals,
            'total_workouts': total_workouts,
            'total_progress_logs': total_progress,
        }
        cache.set(cache_key, data, 60 * 5)  # Cache for 5 minutes
    return Response(data)
