
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Avg, Count, Sum
from .models import NutritionLog, ProgressLog

class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "nutrition/analytics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_meals'] = NutritionLog.objects.filter(user=self.request.user).count()
        context['average_calories'] = NutritionLog.objects.filter(user=self.request.user).aggregate(Avg('calories'))['calories__avg']
        context['total_workouts'] = ProgressLog.objects.filter(user=self.request.user).count()
        return context
