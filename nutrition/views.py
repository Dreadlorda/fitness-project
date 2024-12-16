
from rest_framework.viewsets import ModelViewSet
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import NutritionLog
from .serializers import NutritionLogSerializer

class NutritionLogViewSet(ModelViewSet):
    queryset = NutritionLog.objects.select_related('user').all()
    serializer_class = NutritionLogSerializer

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
