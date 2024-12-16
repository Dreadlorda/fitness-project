
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.select_related('user').all()
    serializer_class = WorkoutSerializer

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
