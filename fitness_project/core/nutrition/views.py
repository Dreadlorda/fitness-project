
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.db.models import Avg, Count, Sum
from .models import NutritionLog, ProgressLog

class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "fitness_project.core.nutrition/analytics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_meals'] = NutritionLog.objects.filter(user=self.request.user).count()
        context['average_calories'] = NutritionLog.objects.filter(user=self.request.user).aggregate(Avg('calories'))['calories__avg']
        context['total_workouts'] = ProgressLog.objects.filter(user=self.request.user).count()
        return context

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, FormView
from django.urls import reverse_lazy
from .models import ProgressLog, NutritionLog
from .forms import UserSettingsForm


# ProgressLogListView
class ProgressLogListView(LoginRequiredMixin, ListView):
    model = ProgressLog
    template_name = "nutrition/progress_log_list.html"
    context_object_name = "progress_logs"

    def get_queryset(self):
        return ProgressLog.objects.filter(user=self.request.user).order_by("-date")


# LeaderboardView
class LeaderboardView(LoginRequiredMixin, ListView):
    model = NutritionLog
    template_name = "nutrition/leaderboard.html"
    context_object_name = "leaderboard"

    def get_queryset(self):
        return (
            NutritionLog.objects.values("user__username")
            .annotate(total_calories=Sum("calories"))
            .order_by("-total_calories")[:10]  # Top 10 users
        )


# UserSettingsView
class UserSettingsView(LoginRequiredMixin, FormView):
    template_name = "nutrition/user_settings.html"
    form_class = UserSettingsForm
    success_url = reverse_lazy("user-settings")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_profile = self.request.user.profile  # Assuming a UserProfile exists
        kwargs["initial"] = {
            "enable_notifications": user_profile.enable_notifications,
            "daily_calorie_goal": user_profile.daily_calorie_goal,
        }
        return kwargs

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)


