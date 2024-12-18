from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.db.models import Sum, Avg, Count
from django.contrib import messages
from django.http import HttpResponse
from reportlab.pdfgen import canvas

from .forms import GoalForm
from fitness_project.core.nutrition.models import ProgressLog
from .models import Goal
from ..workouts.models import Workout, Streak, Notification, Badge


class GoalListView(LoginRequiredMixin, generic.ListView):
    model = Goal
    template_name = 'goals/goal_list.html'
    context_object_name = 'goals'

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

class GoalCreateView(LoginRequiredMixin, generic.CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'workouts/goal_form.html'
    success_url = reverse_lazy('goal-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GoalUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'workouts/goal_form.html'
    success_url = reverse_lazy('goal-list')

class GoalDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Goal
    template_name = 'workouts/goal_confirm_delete.html'
    success_url = reverse_lazy('goal-list')

class AnalyticsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'analytics/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_goals'] = Goal.objects.filter(user=self.request.user).count()
        context['total_progress'] = ProgressLog.objects.filter(user=self.request.user).aggregate(total_progress=Sum('progress'))['total_progress']
        context['total_workouts'] = Workout.objects.filter(user=self.request.user).count()
        return context

@login_required
def update_streak(request):
    streak, created = Streak.objects.get_or_create(user=request.user)
    streak.update_streak()
    Notification.objects.create(user=request.user, message=f"Your streak has been updated! Current Streak is {streak.current_streak} days.")
    messages.success(request, f"Your streak has been updated! Current Streak is {streak.current_streak} days.")
    return redirect('workout-list')

@login_required
def award_badges(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    if streak.current_streak == 7:
        badge, created = Badge.objects.get_or_create(name='7-Day Streak', defaults={'description': 'Completed a 7-day streak'})
        if created:
            badge.save()
        Notification.objects.create(user=request.user, message="Congratulations! You've earned the '7-Day Streak' badge!")
        messages.success(request, "Congratulations! You've earned the '7-Day Streak' badge!")
    return redirect('workout-list')

@login_required
def leaderboard(request):
    top_users = Streak.objects.order_by('-current_streak')[:10]
    return render(request, 'workouts/leaderboard.html', {'top_users': top_users})

@login_required
def generate_progress_report(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="progress_report.pdf"'
    p = canvas.Canvas(response)
    p.drawString(100, 800, f"Progress Report for {request.user.username}")

    streak, _ = Streak.objects.get_or_create(user=request.user)
    p.drawString(100, 770, f"Current Streak: {streak.current_streak} days")
    p.drawString(100, 750, f"Longest Streak: {streak.longest_streak} days")

    workouts = Workout.objects.filter(user=request.user)
    y = 730
    p.drawString(100, y, "Workout Summary:")
    for workout in workouts:
        y -= 20
        if y < 50:
            p.showPage()
            y = 800
        p.drawString(100, y, f"{workout.name}: {workout.duration} mins, {workout.calories_burned} calories")

    p.showPage()
    p.save()
    return response

@login_required
def activity_recommendations(request):
    user_workouts = Workout.objects.filter(user=request.user)
    avg_duration = user_workouts.aggregate(Avg('duration'))['duration__avg'] or 0
    avg_calories = user_workouts.aggregate(Avg('calories_burned'))['calories_burned__avg'] or 0

    recommendations = []
    if avg_duration < 30:
        recommendations.append("Try increasing your workout duration to at least 30 minutes.")
    if avg_calories < 300:
        recommendations.append("Focus on high-intensity workouts to burn more calories.")
    if user_workouts.count() < 3:
        recommendations.append("Aim to work out at least 3 times a week to build consistency.")

    context = {
        'recommendations': recommendations,
        'avg_duration': avg_duration,
        'avg_calories': avg_calories,
    }
    return render(request, 'workouts/recommendations.html', context)

@login_required
def dashboard(request):
    streak, _ = Streak.objects.get_or_create(user=request.user)
    total_calories = Workout.objects.filter(user=request.user).aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
    total_workouts = Workout.objects.filter(user=request.user).count()

    context = {
        'streak': streak,
        'total_calories': total_calories,
        'total_workouts': total_workouts,
    }
    return render(request, 'workouts/dashboard.html', context)