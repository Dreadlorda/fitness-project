from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, FormView
from django.db.models import Avg, Sum
from django.urls import reverse_lazy
from users.forms import UserSettingsForm
from .models import NutritionLog, ProgressLog
from users.models import Profile


class AnalyticsView(LoginRequiredMixin, TemplateView):
    template_name = "nutrition/analytics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_meals'] = NutritionLog.objects.filter(user=self.request.user).count()
        context['average_calories'] = NutritionLog.objects.filter(user=self.request.user).aggregate(Avg('calories'))['calories__avg']
        context['total_workouts'] = ProgressLog.objects.filter(user=self.request.user).count()
        return context

class ProgressLogListView(LoginRequiredMixin, ListView):
    model = ProgressLog
    template_name = "nutrition/progress_log_list.html"
    context_object_name = "progress_logs"

    def get_queryset(self):
        return ProgressLog.objects.filter(user=self.request.user).order_by("-date")

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

class UserSettingsView(LoginRequiredMixin, FormView):
    template_name = "nutrition/user_settings.html"
    form_class = UserSettingsForm
    success_url = reverse_lazy("user-settings")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_profile, created = Profile.objects.get_or_create(user=self.request.user)
        kwargs["initial"] = {
            "enable_notifications": getattr(user_profile, 'enable_notifications', False),
            "daily_calorie_goal": getattr(user_profile, 'daily_calorie_goal', 0),
        }
        return kwargs

    def form_valid(self, form):
        form.save(self.request.user)
        return super().form_valid(form)