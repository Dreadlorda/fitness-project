from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from goals.models import Goal
from workouts.models import Workout

class AsyncGoalAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            goals = Goal.objects.filter(user=request.user).values('id', 'title', 'description', 'goal_type', 'progress', 'target')
            return JsonResponse({"goals": list(goals)}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

class AsyncWorkoutAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            workouts = Workout.objects.filter(user=request.user).values('id', 'exercise_type', 'sets', 'reps', 'duration', 'date')
            return JsonResponse({"workouts": list(workouts)}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
